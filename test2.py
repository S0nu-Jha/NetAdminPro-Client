from ui_ClientInterface import *
from PySide2.QtWidgets import QMessageBox, QMainWindow, QApplication
import sys
import socket
import threading
import subprocess

class Client(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.show()

        # Existing socket for the first code
        self.sock = socket.socket()

        # Connect existing button to the existing function
        self.ui.InfoConnectBTn.clicked.connect(self.connectButtonClicked)

    def connectButtonClicked(self):
        pc_name = self.ui.PcName.text()
        client_ip = self.ui.InfoClientIpAddr.text()
        server_ip = self.ui.InfoServerIpAddr.text()
        server_port = self.ui.InfoServerPort.text()

        if not all([pc_name, client_ip, server_ip, server_port]):
            QMessageBox.warning(self, "Warning", "Please fill in all fields.")
            return

        try:
            # Connect to the server
            self.sock.connect((server_ip, int(server_port)))

            # Send client information to the server
            info_str = f"PC Name: {pc_name}\nClient IP: {client_ip}"
            self.sock.send(info_str.encode())

            # Start receiving commands in a new thread
            receive_command_thread = threading.Thread(target=self.receiveCommand)
            receive_command_thread.daemon = True
            receive_command_thread.start()
        except Exception as e:
            QMessageBox.warning(self, "Connection Error", f"Failed to connect: {str(e)}")
            return

    def receiveCommand(self):
        while True:
            data = self.sock.recv(1024)
            data = data.decode()
            if data:
                # Update your UI or perform any necessary action with the received command
                print("Received command:", data)
                # Execute command received from server (you might need to adapt this based on your needs)
                result = subprocess.Popen(data, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                          stdin=subprocess.PIPE)
                result = result.communicate()
                self.sock.send(result[0])

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Client()
    sys.exit(app.exec_())

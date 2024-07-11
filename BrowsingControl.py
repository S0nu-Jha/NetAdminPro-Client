import socket
import os
import ctypes
import sys

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def receive_command(server_socket):
    while True:
        command = server_socket.recv(1024).decode()

        if command.startswith("BLOCK"):
            # Extract the URL from the command and block it
            url_to_block = command.split(" ")[1]
            block_website(url_to_block)

def block_website(url):
    try:
        # Check if the script has admin rights
        if not is_admin():
            print("Script does not have admin rights.")
            # Re-run the script with admin rights
            ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
            sys.exit()

        # Get the path to the hosts file
        hosts_path = os.path.join(os.environ['SystemRoot'], 'System32', 'drivers', 'etc', 'hosts')

        # Open the hosts file in append mode and add the blocked website entry
        with open(hosts_path, 'a') as hosts_file:
            hosts_file.write(f"127.0.0.1 {url}\n")

        print(f"Website {url} blocked successfully.")
    except Exception as e:
        print(f"Error blocking website: {e}")

# Add this line to your code to print the hosts file path
print("Hosts file path:", os.path.join(os.environ['SystemRoot'], 'System32', 'drivers', 'etc', 'hosts'))

def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('192.168.0.107', 5033))

    # Receive commands from the server
    receive_command(client)

if __name__ == "__main__":
    main()

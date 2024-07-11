import socket
import win32evtlog
import ctypes
import sys
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def run_with_admin_privileges():
    if ctypes.windll.shell32.IsUserAnAdmin() == 0:
        # Request admin rights
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
    else:
        print("Admin privileges granted.")

run_with_admin_privileges()

def read_logs(log_type):
    computer = "192.168.43.66"
    log = win32evtlog.OpenEventLog(computer, log_type)
    flags = win32evtlog.EVENTLOG_BACKWARDS_READ | win32evtlog.EVENTLOG_SEQUENTIAL_READ
    events = []

    while True:
        raw_events = win32evtlog.ReadEventLog(log, flags, 0)
        if not raw_events:
            break
        for event in raw_events:
            events.append(event.StringInserts)  # Adjust for specific log information

    return events


def create_pdf(logs):
    c = canvas.Canvas("received_logs.pdf")
    y_offset = 800
    for log in logs:
        if isinstance(log, tuple):
            log = log[0]  # Assuming log is a tuple, we extract the string value
        c.drawString(100, y_offset, str(log))
        y_offset -= 20  # Adjusting the vertical position for the next log entry
    c.save()
    return "received_logs.pdf"


def send_pdf(pdf_filename):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('192.168.43.66', 4444))  # Replace with the server's host and port

    with open(pdf_filename, 'rb') as file:
        file_data = file.read(1024)
        while file_data:
            client.send(file_data)
            file_data = file.read(1024)

    client.close()

logs = read_logs("Application")
pdf_file = create_pdf(logs)
send_pdf(pdf_file)

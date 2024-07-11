import socket
import os

def sanitize_filename(filename):
    # Replace invalid characters with underscores
    return "".join([c if c.isalnum() or c in ['.', '_', '-'] else '_' for c in filename])

def receive_file(conn):
    # Receive file name as bytes
    file_name_bytes = conn.recv(1024)
    file_name = file_name_bytes.decode('utf-8').rstrip('\x00')  # Strip null characters
    print(f"Original File Name: {file_name}")

    # Sanitize the filename
    sanitized_file_name = sanitize_filename(file_name)
    print(f"Sanitized File Name: {sanitized_file_name}")

    # Receive file size as bytes
    file_size_bytes = conn.recv(8)
    file_size = int.from_bytes(file_size_bytes, byteorder='big')

    with open(sanitized_file_name, 'wb') as file:
        received = 0
        while received < file_size:
            data = conn.recv(1024)
            if not data:
                break
            file.write(data)
            received += len(data)

    print(f"File received successfully: {sanitized_file_name}")
    

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('192.168.0.106', 9097))
receive_file(client)

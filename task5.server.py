import socket
import threading

def handle_client(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode("utf-8")
            if not message:
                break
            print(f"Received message from {client_address}: {message}")
            client_socket.sendall(message.encode("utf-8"))
        except Exception as e:
            print(e)
            break

    client_socket.close()

server_ip = "127.0.0.1"
server_port = 12345
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((server_ip, server_port))
server_socket.listen(1)
print(f"Server listening on {server_ip}:{server_port}")

while True:
    client_socket, client_address = server_socket.accept()
    print(f"New connection from {client_address}")
    client_thread = threading.Thread(target=handle_client, args=(client_socket,))
    client_thread.start()
import socket
import threading

def handle_client(client_socket, client_address):
    print(f"Accepted connection from {client_address}")

    while True:
        try:
            # Receive message from client
            data = client_socket.recv(1024)
            if not data:
                break
            message = data.decode("utf-8")
            print(f"Received message from {client_address}: {message}")

            # Send message to all clients except the sender
            broadcast(message, client_socket)

        except Exception as e:
            print(f"Error: {e}")
            break

 
    print(f"Connection from {client_address} closed.")
    client_socket.close()

def broadcast(message, sender_socket=None):
    for client in clients:
        if client != sender_socket:
            try:
                client.send(message.encode("utf-8"))
            except Exception as e:
                print(f"Error broadcasting message: {e}")

def send_message():
    while True:
        message = input("Enter message to broadcast: ")
        broadcast(message)


server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


server_address = ('localhost', 12345)
server_socket.bind(server_address)


server_socket.listen(5)
print("Server is listening for incoming connections...")


clients = []

send_thread = threading.Thread(target=send_message)
send_thread.start()

while True:
    client_socket, client_address = server_socket.accept()
    clients.append(client_socket)

    client_thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
    client_thread.start()

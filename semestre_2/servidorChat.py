import socket
import threading

clientes = {}  # Dictionary to store clientes and their nicknames
salas = {}  # Dictionary to store salas and their clientes

def broadcast(message, sala, client_socket):
    for client in salas[sala]:
        if client != client_socket:
            client.send(message)

def handle_client(client_socket, client_address):
    client_socket.send("Digite seu apelido: ".encode())
    nickname = client_socket.recv(1024).decode()
    client_socket.send("Digite o nome da sala: ".encode())
    sala = client_socket.recv(1024).decode()

    if sala not in salas:
        salas[sala] = []
    salas[sala].append(client_socket)
    clientes[client_socket] = (nickname, sala)

    print(f"{nickname} se juntou à sala {sala} de {client_address}")
    broadcast(f"{nickname} se juntou à sala!".encode(), sala, client_socket)

    while True:
        try:
            message = client_socket.recv(1024)
            if message:
                formatted_message = f"{nickname}: {message.decode()}"
                print(formatted_message)
                broadcast(formatted_message.encode(), sala, client_socket)
            else:
                remove_client(client_socket, sala)
                break
        except:
            remove_client(client_socket, sala)
            break

def remove_client(client_socket, sala):
    if client_socket in clientes:
        nickname, _ = clientes[client_socket]
        salas[sala].remove(client_socket)
        broadcast(f"{nickname} saiu da sala.".encode(), sala, client_socket)
        print(f"{nickname} desconectado")
        del clientes[client_socket]
    client_socket.close()

def main():
    server_ip = '127.0.0.1'
    server_port = 12345
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((server_ip, server_port))
    server_socket.listen(5)
    print(f"Servidor de chat em execução em {server_ip}:{server_port}")

    while True:
        client_socket, client_address = server_socket.accept()
        client_handler = threading.Thread(target=handle_client, args=(client_socket, client_address))
        client_handler.start()

if __name__ == "__main__":
    main()

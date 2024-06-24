import socket
import threading

def recebendoMensagem(client_socket):
    while True:
        try:
            mensagem = client_socket.recv(1024).decode()
            if mensagem:
                print(mensagem)
            else:
                break
        except:
            break

def main():
    server_ip = '127.0.0.1'
    server_port = 12345
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((server_ip, server_port))

    apelido = input("Digite seu apelido: ")
    sala = input("Digite o nome da sala: ")

    client_socket.send(apelido.encode())
    client_socket.send(sala.encode())

    thread = threading.Thread(target=recebendoMensagem, args=(client_socket,))
    thread.start()

    while True:
        mensagem = input()
        if mensagem.lower() == 'sair':
            client_socket.close()
            break
        client_socket.send(mensagem.encode())

if __name__ == "__main__":
    main()

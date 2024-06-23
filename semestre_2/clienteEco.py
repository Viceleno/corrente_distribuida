import socket

def main():
    server_ip = '127.0.0.1'
    server_port = 12345
    cliente_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    cliente_socket.connect((server_ip, server_port))

    try:
        while True:
            mensagem = input("Digite a mensagem para enviar ao servidor (ou 'sair' para finalizar): ")
            if mensagem.lower() == 'sair':
                break
            cliente_socket.send(mensagem.encode())
            eco_mensagem = cliente_socket.recv(1024).decode()
            print(f"Resposta do servidor: {eco_mensagem}")
    finally:
        cliente_socket.close()

if __name__ == "__main__":
    main()

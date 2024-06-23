import socket
import threading

def identificador_cliente(cliente_socket, endereco_cliente):
    print(f"Conexão recebida de {endereco_cliente}")
    while True:
        try:
            mensagem = cliente_socket.recv(1024).decode()
            if not mensagem:
                break
            print(f"Recebido de {endereco_cliente}: {mensagem}")
            cliente_socket.send(mensagem.encode())
        except ConnectionResetError:
            break
    cliente_socket.close()
    print(f"Conexão encerrada com {endereco_cliente}")

def main():
    server_ip = '127.0.0.1'
    server_port = 12345
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((server_ip, server_port))
    server_socket.listen(5)
    print(f"Servidor de eco em execução em {server_ip}:{server_port}")

    while True:
        cliente_socket, endereco_cliente = server_socket.accept()
        cliente_identificador = threading.Thread(target=identificador_cliente, args=(cliente_socket, endereco_cliente))
        cliente_identificador.start()

if __name__ == "__main__":
    main()

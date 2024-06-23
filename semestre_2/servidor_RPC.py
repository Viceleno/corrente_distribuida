
from xmlrpc.server import SimpleXMLRPCServer

class Operacao_Matematica:
    def adicao(self, x, y):
        return x + y
    
    def subtracao(self, x, y):
        return x - y
    
    def multiplicacao(self, x, y):
        return x * y
    
    def divisao(self, x, y):
        if y == 0:
            return "Erro: Dividido por zero"
        return x / y

def main():
    server = SimpleXMLRPCServer(("localhost", 8000))
    server.register_instance(Operacao_Matematica())
    print("Server is running on port 8000...")
    server.serve_forever()

if __name__ == "__main__":
    main()

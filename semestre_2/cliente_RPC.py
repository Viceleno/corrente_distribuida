
import xmlrpc.client


def main():
    server = xmlrpc.client.ServerProxy("http://localhost:8000/")

    while True:
        print("Escolha a operação:")
        print("1. Soma")
        print("2. Subtração")
        print("3. Multiplicação")
        print("4. Divisão")
        print("5. Sair")

        Escolha = input("Digite a sua escolha (1/2/3/4/5): ")

        if Escolha == '5':
            break

        if Escolha in ['1', '2', '3', '4']:
            try:
                x = float(input("Digite o primeiro número: "))
                y = float(input("Digite o segundo número: "))
            except ValueError:
                print("Erro: Entrada inválida. Por favor, digite números válidos.")
                continue

            if Escolha == '1':
                resultado = server.adicao(x, y)
            elif Escolha == '2':
                resultado = server.subtracao(x, y)
            elif Escolha == '3':
                resultado = server.multiplicacao(x, y)
            elif Escolha == '4':
                resultado = server.divisao(x, y)

            print(f"Resultado: {resultado}")
        else:
            print("Escolha inválida, por favor tente novamente.")

        continuar = input(
            "Deseja continuar fazendo operações? (sim/não): ").strip().lower()
        if continuar not in ['sim', 's']:
            break


if __name__ == "__main__":
    main()

import random 
import threading
from datetime import datetime

numero_sorteado = 0
numero_encontrado = False
numero_maximo = 1000

def gerarNumeroAleatorio():
    global numero_sorteado
    numero_sorteado = random.randint(1,numero_maximo)
    print("Numero Sorteado: ", numero_sorteado)

def descobriNumeroGerado():
    global numero_sorteado, numero_encontrado
    chute_inicial = int(numero_maximo/2)
    chute = chute_inicial

    while not numero_encontrado:
        print(threading.current_thread().name," ", chute)
        if chute < numero_sorteado:
            chute += 1
        elif chute > numero_sorteado:
            chute -= 1

        else:
            print("Numero encontrado pela thread", threading.current_thread().name)
            numero_encontrado = True
            break

def main():
    gerarNumeroAleatorio()

    thread1 = threading.Thread(target=descobriNumeroGerado, name="Thread 1")
    thread2 = threading.Thread(target=descobriNumeroGerado, name="Thread 2")

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

inicio = datetime.now()
main()
print(datetime.now() - inicio)
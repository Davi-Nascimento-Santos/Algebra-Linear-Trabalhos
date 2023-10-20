import random
import main

def gerar_matriz_randomica():
    matriz = []
    for i in range(4):
        vetor = []
        for j in range(4):
            if i == j:
                vetor.append(0)
            else:
                vetor.append(random.randint(0, 1))
        matriz.append(vetor)
    return matriz


def gerar_matriz_escrita():
    matriz = []
    for i in range(4):
        vetor = []
        for j in range(4):
            while True:
                num = int(input('Digite o número entre 0 e 1: '))
                if i == j and num == 0:
                    print('O número que você digitou está incorreto, tente novamente')
                else:
                    vetor.append(num)
                    break
        matriz.append(vetor)
    return matriz

def mult_matriz(matriz):
    matrizResultante = []
    for i in range(len(matriz)):
        posi = 0
        temp = []
        for k in range(len(matriz[i])):
            sum = 0 
            for j in range(len(matriz[i])):
                sum += matriz[i][j] * matriz[j][posi]
            posi += 1
            temp.append(sum)
        matrizResultante.append(temp)
    return matrizResultante

def show(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if j < len(matriz[i])-1:
                print(matriz[i][j], end=" ")
            else:
                print(matriz[i][j])

matriz_proposta = [[0, 1, 1, 1, 1],
                   [1, 0, 1, 1, 0],
                   [0, 1, 0, 1, 0],
                   [0, 0, 1, 0, 1],
                   [0, 0, 0, 1, 0]]

#print(show(mult_matriz(matriz_proposta)))
teste = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
t = [[1, 2], [3, 4]]
for i in range(2):
    t = mult_matriz(t)
    show(t)
#show(mult_matriz(t))
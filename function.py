import random
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

def pathCalc(matriz, b, e):
    oneWay = []
    twoWay =[]
    threeWay = []
    fourWay = []
    for i in range(len(matriz[b])):
        if matriz[b][i] == 1:
            if i == e:
                oneWay.append([b+1,e+1])
            elif matriz[i][e] == 1:
                twoWay.append([b+1, i+1, e+1])
            for j in range(len(matriz[i])):
                if matriz[i][j] == 1:
                    if matriz[j][e] == 1 and b != j and i != e and j != e:
                        threeWay.append([b+1, i+1, j+1, e+1])
                    for k in range(len(matriz[j])):
                        if matriz[j][k] == 1 and matriz[k][e] == 1:
                            find = False
                            path = [b, i, j, k, e]
                            trash = []
                            for z in path:
                                if z not in trash:
                                    trash.append(z)
                                else:
                                    find = True
                                    break
                            if find == False:
                                fourWay.append([b+1, i+1, j+1, k+1, e+1])
    return [oneWay, twoWay, threeWay, fourWay]

#b != j and i != e and j != e and j != b and k != e and k != b
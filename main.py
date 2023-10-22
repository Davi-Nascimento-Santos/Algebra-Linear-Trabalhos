from function import *
matriz_proposta = [[0, 1, 1, 1, 1],
                   [1, 0, 1, 1, 0],
                   [0, 1, 0, 1, 0],
                   [0, 0, 1, 0, 1],
                   [0, 0, 0, 1, 0]]

#li = int(input("Digite a torre de transmissão L_i: "))
#lj = int(input("Digite a torre de transmissão L_j: "))
matriz = [[0, 1, 1],
          [0, 0, 1],
          [1, 1, 0]]
#show(mult_matriz(matriz_proposta))
oneWay = []
twoWay =[]
threeWay = []
"""for i in range(len(matriz_proposta[li-1])):
    if matriz_proposta[li-1][i] == 1:
        if i == lj-1:
            oneWay.append([li,lj])
        elif matriz_proposta[i][lj-1] == 1:
            twoWay.append([li, i+1, lj])
        for k in range(len(matriz_proposta[i])):
            if matriz_proposta[i][k] == 1 and li-1 != k and i != lj-1 and k != lj-1:
                if matriz_proposta[k][lj-1] == 1:
                    threeWay.append([li, i+1, k+1, lj])"""

resul = pathCalc(matriz_proposta, 0, 1)
for i in range(4):
    print(resul[i])
#print(oneWay)
#print(twoWay)
#print(threeWay)


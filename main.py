from function import *
while True:
    op = int(input("""Selecione umas dessas três opções:\n1 - Matriz original\n2 - Matriz randomica\n3 - Inserir a matriz\n4 - Sair do programa\nopção: """))
    if 1 <= op <= 4:
        if op == 1:
            matriz = matriz_proposta
        elif op == 2:
            matriz = gerar_matriz_randomica()
        elif op == 3:
            matriz = gerar_matriz_escrita()
        else:
            break
        print("Matriz usada como base: ")
        show(matriz)
        while True:
            li = int(input("Digite o número da torre de transmissão Li: "))
            lj = int(input("Digite o número da torre de transmissão Lj: "))
            if  li > 5 or li < 1 or lj < 1 or lj > 5:
                print("ERRO! Digite valores entre 1 e 5")
            else:
                break
        while True:
            opt = int(input("Digite quantas formas de retransmissão você deseja que sejam exibidas:\n(1) com transmissão direta entre Li e Lj\n(2) com no máximo uma retransmissão\n(3) com no máximo duas retransmissões\n(4) com no máximo três retransmissões\n(5) todas as retransmissões possiveis\nOpção: "))
            if 1 <= opt <= 5:
                break
            else:
                print("Erro! Digite uma opção correta!")        
        resul = pathCalc(matriz, li-1, lj-1)
        if opt <= 4:
            print(f"{opt} Transmissões:")
            if len(resul[opt-1]) == 0:
                print("Não há transmissões!")
            for i in range(len(resul[opt-1])):
                for j in range(len(resul[opt-1][i])):
                    print(resul[opt-1][i][j], end="")
                    if j < len(resul[opt-1][i])-1:
                        print(" ->", end=" ")
                    else:
                        print()

        else:
            for t in range(len(resul)):
                print(f"{t+1} Transmissões:")
                if len(resul[t]) == 0:
                        print("Não há transmissões!")
                        break
                for i in range(len(resul[t])):
                    for j in range(len(resul[t][i])):
                        print(resul[t][i][j], end="")
                        if j < len(resul[t][i])-1:
                            print(" ->", end=" ")
                        else:
                            print()
            

    else:
        print("Erro! Digite uma opção correta!")

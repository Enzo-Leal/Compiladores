# nao pode pedir imput, tem que roodar direto
# ler de um arquivo


# na atividade 2 traduzir um arquivo para o trabalho 1

# opcao fazer um programa só, fazendo um ponto no meio pra exibir i resultado

# ideia de OPCODE, zerar um espaço de memoria, lipar as memorias
# gerar um erro e gravar em um arquivo de log em um espaço de memoria

#from winreg import REG_BINARY


MEM_INTRUCOES = []
# Contador de programa
contador_programa = 0

# funcao para ler o arquivo e colocar em um array de "memoria"


def MEM_BIN_PARA_MEM_INSTRUCOES():

    with open("instrucoes_txt.txt", "r") as instrucoes:
        
        for linha in instrucoes:
            MEM_INTRUCOES.append(linha)
            for i in range(len(MEM_INTRUCOES)):
                MEM_INTRUCOES[i] 

# while MEM_INTRUCOES:
    #    print(MEM_INTRUCOES)
    #    MEM_INTRUCOES = file.read(8)


    #with open("instrucoes.bin", "rb") as instrucoes:
    #    for linha in instrucoes:
    #        MEM_INTRUCOES.append(linha.rstrip())

    print(MEM_INTRUCOES)
    print(type(MEM_INTRUCOES[0]))
    


def LER_INSTRUCAO():
    global contador_programa

    TAMANHO_MEM_INTRUCOES = len(MEM_INTRUCOES)

    OP_SOMA = b'10000001'
    OP_SUB = 9998
    OP_MULT = 9997
    OP_DIV = 9996

    while contador_programa < TAMANHO_MEM_INTRUCOES:
        if MEM_INTRUCOES[contador_programa] == OP_SOMA:
            SOMA()
            break
        elif MEM_INTRUCOES[contador_programa] == OP_SUB:
            SUB()
            break
        elif MEM_INTRUCOES[contador_programa] == OP_MULT:
            MULT()
            break
        elif MEM_INTRUCOES[contador_programa] == OP_DIV:
            DIV()
            break
        else:
            contador_programa += 1
            LER_INSTRUCAO()
            break


def SOMA():
    global contador_programa
    contador_programa += 1
    REG_A = bin(MEM_INTRUCOES[contador_programa])
    contador_programa += 1
    REG_B = bin(MEM_INTRUCOES[contador_programa])
    contador_programa += 1
    MEM_INTRUCOES[contador_programa] = bytes(REG_A) + bytes(REG_B)
    contador_programa += 1

    print("DUMP da memoria após soma\n")
    print(MEM_INTRUCOES)

    LER_INSTRUCAO()


def main():
    global contador_programa

    MEM_BIN_PARA_MEM_INSTRUCOES()

    print("DUMP da memoria inicial\n")
    print(MEM_INTRUCOES)

    print("Compilador iniciado")
    LER_INSTRUCAO()


main()

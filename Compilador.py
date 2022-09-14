# OP CODES

# ESPAÇOS DE MEMORIA
MEM = []


contador_programa = 0


def ADICIONAR_MEMORIA():
    global contador_programa
    MEM.append(input("Digite o valor de MEM_A: "))
    MEM.append(input("Digite o valor de MEM_B: "))
    MEM.append(input("Digite o valor de MEM_C: "))
    MEM.append(input("Digite o valor de MEM_D: "))
    print("Memoria adicionada com sucesso")
    return contador_programa


def Ciclo_de_instrucoes():
    global contador_programa

    OP_SOMA = 1000  # Soma 2 numeros e adiciona eles na memoria seguinte
    OP_SUB = 1001  # Subtrai 2 numeros e adiciona eles na memoria seguinte
    OP_FIM = 1999  # Fim do programa

    print("Ciclo de instruções iniciado")

    while contador_programa < len(MEM):
        print(MEM[contador_programa])
        if MEM[contador_programa] == int(OP_SOMA):
            while MEM != OP_FIM:
                contador_programa += 1
                MEM[contador_programa +
                    2] = bin(MEM[contador_programa]) + bin(MEM[contador_programa + 1])
                contador_programa += 1
                main()

        elif MEM[contador_programa] == OP_SUB:
            while MEM != OP_FIM:
                contador_programa += 1
                MEM[contador_programa +
                    2] = bin(MEM[contador_programa]) - bin(MEM[contador_programa + 1])
                contador_programa += 1
                main()


        print("FIM")


def main():
    print("Compilador iniciado")
    print("1 - Adicionar a memoria")
    OPCAO_MENU = input("Digite a opção desejada: ")

    match OPCAO_MENU:
        case "1":
            ADICIONAR_MEMORIA()
            main()
        case "2":
            Ciclo_de_instrucoes()

        case "3":
            print("DUMP de memoria\n MEM_A = ", MEM[0], "\n MEM_B = ", MEM[1], "\n MEM_C = ", MEM[2], "\n MEM_D = ", MEM[3], "\n MEM_E = ",
                  MEM[4], "\n MEM_F = ", MEM[5], "\n MEM_G = ", MEM[6], "\n MEM_H = ", MEM[7], "\n MEM_I = ", MEM[8], "\n MEM_J = ")
        case _:
            print("Opção inválida")


main()

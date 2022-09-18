# OP CODES
OP_SOMA = 1000  # Soma 2 numeros e adiciona eles na memoria seguinte
OP_SUB = 1001  # Subtrai 2 numeros e adiciona eles na memoria seguinte
OP_FIM = 1999  # Fim do programa

# ESPAÇOS DE MEMORIA
MEM_SOMA = ["1000","0001", "0010", "0011", "0100", "0101", "0110", "0111"]
MEM_SUB = ["1001","0001", "0010", "0011", "0100", "0101", "0110", "0111"]

# Contador de programa
contador_programa = 0


def Ciclo_de_instrucoes(ESCOLHA_MEMORIA):
    global contador_programa

    
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
    print("Compilador iniciado\n Digite a instrução desejada\n\n\n 1 - Soma\n 2 - Subtração\n 3 - DUMP de memoria 4 - FIM")

    while True:
        OPCAO_MENU = input("Digite a opção desejada: ")

        match OPCAO_MENU:
            case "1":
                Ciclo_de_instrucoes(MEM_SOMA)
                main()
            case "2":
                Ciclo_de_instrucoes(MEM_SUB)

            case "3":
                print("DUMP de memoria\n MEM_A = ", MEM[0], "\n MEM_B = ", MEM[1], "\n MEM_C = ", MEM[2], "\n MEM_D = ", MEM[3], "\n MEM_E = ",
                      MEM[4], "\n MEM_F = ", MEM[5], "\n MEM_G = ", MEM[6], "\n MEM_H = ", MEM[7], "\n MEM_I = ", MEM[8], "\n MEM_J = ")
            
            case "4":
                print("FIM")
                break
            
            case _:
                print("Opção inválida")


main()

# OP CODES


# ESPAÇOS DE MEMORIA
MEM = [0b1000, 0b0001, 0b0010, 0b0011 , 0b0100, 0b0101, 0b0110, 0b0111]
#MEM_SUB = ["1001", "0001", "0010", "0011", "0100", "0101", "0110", "0111"]

# Contador de programa
contador_programa = 0


def Ciclo_de_instrucoes(ESCOLHA_MEMORIA):
    global contador_programa

    OP_SOMA = 0b1000  # Soma o segundo espaço de memória com o terceiro e armazena o resultado no quarto espaço de memória
    OP_SUB = 1001  # Subtrai 2 numeros e adiciona eles na memoria seguinte
    OP_FIM = 1999  # Fim do programa

    print("Ciclo de instruções iniciado")

    
    while True:
        if ESCOLHA_MEMORIA[contador_programa] == OP_SOMA:
            print("Soma")
            MEM[3] = bin(MEM[1] + MEM[2])
            contador_programa += 1
            print("MEM_A = ", bin(MEM[0]), "\n MEM_B = ", bin(MEM[1]), "\n MEM_C = ", bin(MEM[2]), "\n MEM_D = ", MEM[3], "\n MEM_E = ", bin(MEM[4]), "\n MEM_F = ", bin(MEM[5]))
            main()


        elif ESCOLHA_MEMORIA[contador_programa] == str(OP_SUB):
            print("Subtração")
            MEM[3] = MEM[1] - MEM[2]
            contador_programa += 1
            print("MEM_A = ", bin(MEM[0]), "\n MEM_B = ", bin(MEM[1]), "\n MEM_C = ", bin(MEM[2]), "\n MEM_D = ", MEM[3], "\n MEM_E = ", bin(MEM[4]), "\n MEM_F = ", bin(MEM[5]))

        elif ESCOLHA_MEMORIA[contador_programa] == str(OP_FIM):
            print("Fim")
            break

        else:
            print("Instrução inválida")
            break

   

def main():
    print("Compilador iniciado\n Digite a instrução desejada\n\n\n 1 - Soma\n 2 - Subtração\n 3 - DUMP de memoria 4 - FIM")

    while True:
        OPCAO_MENU = input("Digite a opção desejada: ")

        match OPCAO_MENU:
            case "1":
                Ciclo_de_instrucoes(MEM)
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

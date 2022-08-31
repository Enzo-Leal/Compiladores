#OP CODES
OP_SOMA = 1000
OP_SUB = 1001

#ESPAÇOS DE MEMORIA
MEM_A = 0
MEM_B = 0
MEM_C = 0
MEM_D = 0
MEM_F = 0
MEM_G = 0
MEM_H = 0
MEM_I = 0
MEM_J = 0
MEM_K = 0



contador_programa = 0

def ADICIONAR_MEMORIA():
    espacoDeMemoria = input("Digite o espaço de memória que deseja adicionar(A-K) \n ou 0 para voltar ao menu: ")
    match espacoDeMemoria:
        case "A":
            print("Digite o valor de A em binario")
            MEM_A = input()
            ADICIONAR_MEMORIA()
        case "B":
            print("Digite o valor de B em binario")
            MEM_B = input()
            ADICIONAR_MEMORIA()
        case "C":
            print("Digite o valor de C em binario")
            MEM_C = input()
            ADICIONAR_MEMORIA()
        case "D":
            print("Digite o valor de D em binario")
            MEM_D = input()
            ADICIONAR_MEMORIA()
        case "F":
            print("Digite o valor de F em binario")
            MEM_F = input()
            ADICIONAR_MEMORIA()
        case "G":
            print("Digite o valor de G em binario")
            MEM_G = input()
            ADICIONAR_MEMORIA()
        case "H":
            print("Digite o valor de H em binario")
            MEM_H = input()
            ADICIONAR_MEMORIA()
        case "I":
            print("Digite o valor de I em binario")
            MEM_I = input()
            ADICIONAR_MEMORIA()
        case "J":
            print("Digite o valor de J em binario")
            MEM_J = input()
            ADICIONAR_MEMORIA()
        case "K":
            print("Digite o valor de K em binario")
            MEM_K = input()
            ADICIONAR_MEMORIA()
        case "0":
            main()
        case _:
            print("Opção inválida")
            ADICIONAR_MEMORIA()



def SOMA():
    global contador_programa
    contador_programa += 1
    MEM_A_DEC = int(MEM_A)
    contador_programa += 1
    MEM_B_DEC = int(MEM_B)
    contador_programa += 1
    MEM_C_DEC = MEM_A_DEC + MEM_B_DEC
    contador_programa += 1
    MEM_C = bin(MEM_C_DEC)
    contador_programa += 1
    print("O resultado da soma é: ", MEM_C)

    return contador_programa


def main():
    print("Compilador iniciado")
    print("1 - Adicionar a memoria")
    print("2 - Para SOMAR MEM_A a MEM_B e guardar o resultado em MEM_C")
    print("3 - Para SUBTRAIR MEM_A a MEM_B e guardar o resultado em MEM_C")
    OPCAO_MENU = input("Digite a opção desejada: ")

    match OPCAO_MENU:
        case "1":
            ADICIONAR_MEMORIA();
        case "2":
            SOMA();

        case "3":
            print("Subtração")
        case _:
            print("Opção inválida")


main()

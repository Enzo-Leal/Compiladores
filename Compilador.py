#OP CODES
OP_SOMA = 1000
OP_SUB = 1001

#ESPAÇOS DE MEMORIA
MEM_A = 0
MEM_B = 0



contador_programa = 0

def ADICIONAR_MEMORIA():
    espacoDeMemoria = input("Digite o espaço de memória que deseja adicionar: ")
    match espacoDeMemoria:
        case "A":
            print("Digite o valor de A em binario")
            MEM_A = input()
        case "B":
            print("Digite o valor de B em binario")
            MEM_B = input()


def SOMA():
    contador_programa += 1
    
    return contador_programa


def main():
    print("Compilador iniciado")
    print("1 - Adicionar a memoria")
    print("2 - Para SOMAR MEM_A a MEM_B e guardar o resultado em MEM_C")
    print("3 - Para SUBTRAIR MEM_A a MEM_B e guardar o resultado em MEM_C")
    OPCAO_MENU = input("Digite a opção desejada: ")

    match OPCAO_MENU:
        case "1":
            print("Digite o valor de A em binario")
            MEM_A = input()
            print("Digite o valor de B em binario")
            MEM_B = input()
        case "2":
            print("Soma")

        case "3":
            print("Subtração")
        case _:
            print("Opção inválida")

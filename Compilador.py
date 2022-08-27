OP_SOMA = 1000
OP_SUB = 1001

contador_programa = 0


def SOMA:
    contador_programa += 1

    return contador_programa


def main():
    print("Compilador iniciado")
    print("1 - Para SOMAR MEM_A a MEM_B e guardar o resultado em MEM_C")
    print("2 - Para SUBTRAIR MEM_A a MEM_B e guardar o resultado em MEM_C")
    OPCAO_MENU = input("Digite a opção desejada: ")

    match OPCAO_MENU:
        case 1:
            print("Soma")
        case 2:
            print("Subtração")
        case _:
            print("Opção inválida")

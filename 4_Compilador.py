# nao pode pedir imput, tem que roodar direto
# ler de um arquivo


# na atividade 2 traduzir um arquivo para o trabalho 1

# opcao fazer um programa só, fazendo um ponto no meio pra exibir i resultado

# ideia de OPCODE, zerar um espaço de memoria, lipar as memorias
# gerar um erro e gravar em um arquivo de log em um espaço de memoria


#               Manual de instrucoes

# OPCodes:
#   10000001 - Soma - Soma os 2 endereços de memória e armazena o resultado no endereço de memória seguinte
#   10000010 - Subtracao - Subtrai os 2 endereços de memória e armazena o resultado no endereço de memória seguinte
#   10000011 - Multiplicacao - Multiplica os 2 endereços de memória e armazena o resultado no endereço de memória seguinte
#   10000100 - Divisao - Divide os 2 endereços de memória e armazena o resultado no endereço de memória seguinte
#   10000101 - JMP - Pula para o endereço de memória indicado
#   10000110 - Clear Memory - limpa o proximo endereço de memoria
#   11111111 - Exit - sai do programa
#


MEM_INTRUCOES = []
# Contador de programa
contador_programa = 0


def CONVERTER_RESULTADO(RESULTADO):
    match RESULTADO:
        case 0:
            return "00000000"
        case 1:
            return "00000001"
        case 2:
            return "00000010"
        case 3:
            return "00000011"
        case 4:
            return "00000100"
        case 5:
            return "00000101"
        case 6:
            return "00000110"
        case 7:
            return "00000111"
        case 8:
            return "00001000"
        case 9:
            return "00001001"
        case 10:
            return "00001010"
        case 11:
            return "00001011"
        case 12:
            return "00001100"
        case 13:
            return "00001101"
        case 14:
            return "00001110"
        case 15:
            return "00001111"
        case 16:
            return "00010000"
        case 17:
            return "00010001"
        case 18:
            return "00010010"
        case 19:
            return "00010011"
        case 20:
            return "00010100"
        case 21:
            return "00010101"
        case 22:
            return "00010110"
        case 23:
            return "00010111"
        case 24:
            return "00011000"
        case 25:
            return "00011001"
        case 26:
            return "00011010"
        case 27:
            return "00011011"
        case 28:
            return "00011100"
        case 29:
            return "00011101"
        case 30:
            return "00011110"
        case 31:
            return "00011111"
        case 32:
            return "00100000"
        case 33:
            return "00100001"
        case 34:
            return "00100010"
        case 35:
            return "00100011"
        case 36:
            return "00100100"
        case 37:
            return "00100101"
        case 38:
            return "00100110"
        case 39:
            return "00100111"
        case 40:
            return "00101000"
        case 41:
            return "00101001"
        case 42:
            return "00101010"
        case 43:
            return "00101011"
        case 44:
            return "00101100"
        case 45:
            return "00101101"
        case 46:
            return "00101110"
        case 47:
            return "00101111"
        case 48:
            return "00110000"
        case 49:
            return "00110001"
        case 50:
            return "00110010"
        case 51:
            return "00110011"
        case 52:
            return "00110100"
        case 53:
            return "00110101"
        case 54:
            return "00110110"
        case 55:
            return "00110111"
        case 56:
            return "00111000"
        case 57:
            return "00111001"
        case 58:
            return "00111010"
        case 59:
            return "00111011"
        case 60:
            return "00111100"
        case 61:
            return "00111101"
        case 62:
            return "00111110"
        case 63:
            return "00111111"
        case 64:
            return "01000000"
        case 65:
            return "01000001"
        case 66:
            return "01000010"
        case 67:
            return "01000011"
        case 68:
            return "01000100"
        case 69:
            return "01000101"
        case 70:
            return "01000110"
        case 71:
            return "01000111"
        case 72:
            return "01001000"
        case 73:
            return "01001001"
        case 74:
            return "01001010"
        case 75:
            return "01001011"
        case 76:
            return "01001100"
        case 77:
            return "01001101"
        case 78:
            return "01001110"
        case 79:
            return "01001111"
        case 80:
            return "01010000"
        case 81:
            return "01010001"
        case 82:
            return "01010010"
        case 83:
            return "01010011"
        case 84:
            return "01010100"
        case 85:
            return "01010101"
        case 86:
            return "01010110"
        case 87:
            return "01010111"
        case 88:
            return "01011000"
        case 89:
            return "01011001"
        case 90:
            return "01011010"
        case 91:
            return "01011011"
        case 92:
            return "01011100"
        case 93:
            return "01011101"
        case 94:
            return "01011110"
        case 95:
            return "01011111"
        case 96:
            return "01100000"
        case 97:
            return "01100001"
        case 98:
            return "01100010"
        case 99:
            return "01100011"
        case 100:
            return "01100100"
        case 101:
            return "01100101"
        case 102:
            return "01100110"
        case 103:
            return "01100111"
        case 104:
            return "01101000"
        case 105:
            return "01101001"
        case 106:
            return "01101010"
        case 107:
            return "01101011"
        case 108:
            return "01101100"
        case 109:
            return "01101101"
        case 110:
            return "01101110"
        case 111:
            return "01101111"
        case 112:
            return "01110000"
        case 113:
            return "01110001"
        case 114:
            return "01110010"
        case 115:
            return "01110011"
        case 116:
            return "01110100"
        case 117:
            return "01110101"
        case 118:
            return "01110110"
        case 119:
            return "01110111"
        case 120:
            return "01111000"
        case 121:
            return "01111001"
        case 122:
            return "01111010"
        case 123:
            return "01111011"
        case 124:
            return "01111100"
        case 125:
            return "01111101"
        case 126:
            return "01111110"
        case 127:
            return "01111111"


def MEM_BIN_PARA_MEM_INSTRUCOES():

    with open("3_saida_montador.txt", "r") as instrucoes:

        for linha in instrucoes:
            MEM_INTRUCOES.append(linha.strip())


def LER_INSTRUCAO():
    global contador_programa

    TAMANHO_MEM_INTRUCOES = len(MEM_INTRUCOES)

    OP_SOMA = 10000001
    OP_SUB = 10000010
    OP_MULT = 10000011
    OP_DIV = 10000100
    OP_JMP = 10000101
    OP_CLEAR_MEM = 10000110
    OP_EXIT = 11111111

    while contador_programa <= TAMANHO_MEM_INTRUCOES:

        if MEM_INTRUCOES[contador_programa] == str(OP_SOMA):
            SOMA()
            break
        elif MEM_INTRUCOES[contador_programa] == str(OP_SUB):
            SUB()
            break
        elif MEM_INTRUCOES[contador_programa] == str(OP_MULT):
            MULT()
            break
        elif MEM_INTRUCOES[contador_programa] == str(OP_DIV):
            DIV()
            break
        elif MEM_INTRUCOES[contador_programa] == str(OP_JMP):
            JMP()
            break
        elif MEM_INTRUCOES[contador_programa] == str(OP_CLEAR_MEM):
            CLEAR_MEM()
            break
        elif MEM_INTRUCOES[contador_programa] == str(OP_EXIT):
            # colocar aqui a funcao escrever no arquivo de saida
            with open("5_output.txt", "w") as txt_file:
                for line in MEM_INTRUCOES:
                    txt_file.write(str(line) + "\n")
            break

        else:
            contador_programa += 1
            LER_INSTRUCAO()
            break


def SOMA():
    global contador_programa
    contador_programa += 1
    REG_A = int(MEM_INTRUCOES[contador_programa])
    contador_programa += 1
    REG_B = int(MEM_INTRUCOES[contador_programa])
    contador_programa += 1
    MEM_INTRUCOES[contador_programa] = CONVERTER_RESULTADO(REG_A + REG_B)
    contador_programa += 1

    print("DUMP da memoria após soma\n")
    print(MEM_INTRUCOES)
    LER_INSTRUCAO()


def SUB():
    global contador_programa
    contador_programa += 1
    REG_A = int(MEM_INTRUCOES[contador_programa])
    contador_programa += 1
    REG_B = int(MEM_INTRUCOES[contador_programa])
    contador_programa += 1
    MEM_INTRUCOES[contador_programa] = CONVERTER_RESULTADO(REG_A - REG_B)
    contador_programa += 1

    print("DUMP da memoria após subtração\n")
    print(MEM_INTRUCOES)

    LER_INSTRUCAO()


def MULT():
    global contador_programa
    contador_programa += 1
    REG_A = int(MEM_INTRUCOES[contador_programa])
    contador_programa += 1
    REG_B = int(MEM_INTRUCOES[contador_programa])
    contador_programa += 1
    MEM_INTRUCOES[contador_programa] = CONVERTER_RESULTADO(REG_A * REG_B)
    contador_programa += 1

    print("DUMP da memoria após multiplicação\n")
    print(MEM_INTRUCOES)

    LER_INSTRUCAO()


def DIV():
    global contador_programa
    contador_programa += 1
    REG_A = int(MEM_INTRUCOES[contador_programa])
    contador_programa += 1
    REG_B = int(MEM_INTRUCOES[contador_programa])
    contador_programa += 1
    MEM_INTRUCOES[contador_programa] = CONVERTER_RESULTADO(REG_A / REG_B)
    contador_programa += 1

    print("DUMP da memoria após divisão\n")
    print(MEM_INTRUCOES)

    LER_INSTRUCAO()


def JMP():
    global contador_programa
    contador_programa += 1
    contador_programa = int(MEM_INTRUCOES[contador_programa])
    print("DUMP da memoria após pular o endereço\n")
    print(MEM_INTRUCOES)
    LER_INSTRUCAO()


def CLEAR_MEM():
    global contador_programa
    contador_programa += 1
    MEM_INTRUCOES[contador_programa] = "00000000"
    contador_programa += 1
    print("DUMP da memoria após clear\n")
    print(MEM_INTRUCOES)
    LER_INSTRUCAO()


def main():
    global contador_programa

    MEM_BIN_PARA_MEM_INSTRUCOES()

    print("DUMP da memoria inicial\n")
    print(MEM_INTRUCOES)

    LER_INSTRUCAO()


main()

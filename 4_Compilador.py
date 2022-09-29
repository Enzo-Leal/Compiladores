#Array que vai armazenar as instrucoes
MEM_INTRUCOES = []
# Contador de programa
contador_programa = 0

#Função utilizada para converter inteiros em binarios para que as operacoes possam ser realizadas
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

def CONVERTER_BINARIO_DECIMAL(binario):
    match binario:
        case "00000000":
            return 0
        case "00000001":
            return 1
        case "00000010":
            return 2
        case "00000011":
            return 3
        case "00000100":
            return 4
        case "00000101":
            return 5
        case "00000110":
            return 6
        case "00000111":
            return 7
        case "00001000":
            return 8
        case "00001001":
            return 9
        case "00001010":
            return 10
        case "00001011":
            return 11
        case "00001100":
            return 12
        case "00001101":
            return 13
        case "00001110":
            return 14
        case "00001111":
            return 15
        case "00010000":
            return 16
        case "00010001":
            return 17
        case "00010010":
            return 18
        case "00010011":
            return 19
        case "00010100":
            return 20
        case "00010101":
            return 21
        case "00010110":
            return 22
        case "00010111":
            return 23
        case "00011000":
            return 24
        case "00011001":
            return 25
        case "00011010":
            return 26
        case "00011011":
            return 27
        case "00011100":
            return 28
        case "00011101":
            return 29
        case "00011110":
            return 30
        case "00011111":
            return 31
        case "00100000":
            return 32
        case "00100001":
            return 33
        case "00100010":
            return 34
        case "00100011":
            return 35
        case "00100100":
            return 36
        case "00100101":
            return 37
        case "00100110":
            return 38
        case "00100111":
            return 39
        case "00101000":
            return 40
        case "00101001":
            return 41
        case "00101010":
            return 42
        case "00101011":
            return 43
        case "00101100":
            return 44
        case "00101101":
            return 45
        case "00101110":
            return 46
        case "00101111":
            return 47
        case "00110000":
            return 48
        case "00110001":
            return 49
        case "00110010":
            return 50
        case "00110011":
            return 51
        case "00110100":
            return 52
        case "00110101":
            return 53
        case "00110110":
            return 54
        case "00110111":
            return 55
        case "00111000":
            return 56
        case "00111001":
            return 57
        case "00111010":
            return 58
        case "00111011":
            return 59
        case "00111100":
            return 60
        case "00111101":
            return 61
        case "00111110":
            return 62
        case "00111111":
            return 63
        case "01000000":
            return 64
        case "01000001":
            return 65
        case "01000010":
            return 66
        case "01000011":
            return 67
        case "01000100":
            return 68
        case "01000101":
            return 69
        case "01000110":
            return 70
        case "01000111":
            return 71
        case "01001000":
            return 72
        case "01001001":
            return 73
        case "01001010":
            return 74
        case "01001011":
            return 75
        case "01001100":
            return 76
        case "01001101":
            return 77
        case "01001110":
            return 78
        case "01001111":
            return 79
        case "01010000":
            return 80
        case "01010001":
            return 81
        case "01010010":
            return 82
        case "01010011":
            return 83
        case "01010100":
            return 84
        case "01010101":
            return 85
        case "01010110":
            return 86
        case "01010111":
            return 87
        case "01011000":
            return 88
        case "01011001":
            return 89
        case "01011010":
            return 90
        case "01011011":
            return 91
        case "01011100":
            return 92
        case "01011101":
            return 93
        case "01011110":
            return 94
        case "01011111":
            return 95
        case "01100000":
            return 96
        case "01100001":
            return 97
        case "01100010":
            return 98
        case "01100011":
            return 99
        case "01100100":
            return 100
        case "01100101":
            return 101
        case "01100110":
            return 102
        case "01100111":
            return 103
        case "01101000":
            return 104
        case "01101001":
            return 105
        case "01101010":
            return 106
        case "01101011":
            return 107
        case "01101100":
            return 108
        case "01101101":
            return 109
        case "01101110":
            return 110
        case "01101111":
            return 111
        case "01110000":
            return 112
        case "01110001":
            return 113
        case "01110010":
            return 114
        case "01110011":
            return 115
        case "01110100":
            return 116
        case "01110101":
            return 117
        case "01110110":
            return 118
        case "01110111":
            return 119
        case "01111000":
            return 120
        case "01111001":
            return 121
        case "01111010":
            return 122
        case "01111011":
            return 123
        case "01111100":
            return 124
        case "01111101":
            return 125
        case "01111110":
            return 126
        case "01111111":
            return 127


#Função que pegar as instrucoes do arquivo "3_saida_montador.txt" e adiciona ao array MEM_INSTRUCOES
def MEM_BIN_PARA_MEM_INSTRUCOES():

    with open("3_saida_montador.txt", "r") as instrucoes:

        for linha in instrucoes:
            MEM_INTRUCOES.append(linha.strip())


def SOMA():
    global contador_programa
    contador_programa += 1
    REG_A = MEM_INTRUCOES[contador_programa]
    contador_programa += 1
    REG_B = MEM_INTRUCOES[contador_programa]
    contador_programa += 1
    MEM_INTRUCOES[contador_programa] = CONVERTER_RESULTADO(int(CONVERTER_BINARIO_DECIMAL(REG_A)) + int(CONVERTER_BINARIO_DECIMAL(REG_B)))
    contador_programa += 1
    LER_INSTRUCAO()


def SUB():
    global contador_programa
    contador_programa += 1
    REG_A = MEM_INTRUCOES[contador_programa]
    contador_programa += 1
    REG_B = MEM_INTRUCOES[contador_programa]
    contador_programa += 1
    MEM_INTRUCOES[contador_programa] = CONVERTER_RESULTADO(int(CONVERTER_BINARIO_DECIMAL(REG_A)) + int(CONVERTER_BINARIO_DECIMAL(REG_B)))
    contador_programa += 1
    LER_INSTRUCAO()


def MULT():
    global contador_programa
    contador_programa += 1
    REG_A = MEM_INTRUCOES[contador_programa]
    contador_programa += 1
    REG_B = MEM_INTRUCOES[contador_programa]
    contador_programa += 1
    MEM_INTRUCOES[contador_programa] = CONVERTER_RESULTADO(int(CONVERTER_BINARIO_DECIMAL(REG_A)) + int(CONVERTER_BINARIO_DECIMAL(REG_B)))
    contador_programa += 1
    LER_INSTRUCAO()


def DIV():
    global contador_programa
    contador_programa += 1
    REG_A = MEM_INTRUCOES[contador_programa]
    contador_programa += 1
    REG_B = MEM_INTRUCOES[contador_programa]
    contador_programa += 1
    MEM_INTRUCOES[contador_programa] = CONVERTER_RESULTADO(int(CONVERTER_BINARIO_DECIMAL(REG_A)) + int(CONVERTER_BINARIO_DECIMAL(REG_B)))
    contador_programa += 1
    LER_INSTRUCAO()


def JMP():
    global contador_programa
    contador_programa += 1
    contador_programa = int(MEM_INTRUCOES[contador_programa])
    LER_INSTRUCAO()


def CLEAR_MEM():
    global contador_programa
    contador_programa += 1
    MEM_INTRUCOES[contador_programa] = "00000000"
    contador_programa += 1
    LER_INSTRUCAO()


#Função que irá percorrer a memoria e executar o que for nescessario
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


def main():
    print("Programa iniciado")
    MEM_BIN_PARA_MEM_INSTRUCOES()
    LER_INSTRUCAO()
    print("Programa finalizado")


main()

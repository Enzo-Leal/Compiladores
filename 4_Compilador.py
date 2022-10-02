#Array que vai armazenar as instrucoes
MEM_INTRUCOES = []
# Contador de programa
contador_programa = 0

#Função utilizada para converter inteiros em binarios para que as operacoes possam ser realizadas
def CONVERTER_RESULTADO(RESULTADO):
    return format(RESULTADO, '08b')

#nao pode trocar essa funcao por conversoes bin->dec pois se nao quebra a formatacao e nao funcionam as operacoes
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
    MEM_INTRUCOES[contador_programa] = CONVERTER_RESULTADO(int(CONVERTER_BINARIO_DECIMAL(REG_A)) - int(CONVERTER_BINARIO_DECIMAL(REG_B)))
    contador_programa += 1
    LER_INSTRUCAO()


def MULT():
    global contador_programa
    contador_programa += 1
    REG_A = MEM_INTRUCOES[contador_programa]
    contador_programa += 1
    REG_B = MEM_INTRUCOES[contador_programa]
    contador_programa += 1
    MEM_INTRUCOES[contador_programa] = CONVERTER_RESULTADO(int(CONVERTER_BINARIO_DECIMAL(REG_A)) * int(CONVERTER_BINARIO_DECIMAL(REG_B)))
    contador_programa += 1
    LER_INSTRUCAO()


def DIV():
    global contador_programa
    contador_programa += 1
    REG_A = MEM_INTRUCOES[contador_programa]
    contador_programa += 1
    REG_B = MEM_INTRUCOES[contador_programa]
    contador_programa += 1
    MEM_INTRUCOES[contador_programa] = CONVERTER_RESULTADO(int(CONVERTER_BINARIO_DECIMAL(REG_A)) / int(CONVERTER_BINARIO_DECIMAL(REG_B)))
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

# nao pode pedir imput, tem que roodar direto
# ler de um arquivo


# na atividade 2 traduzir um arquivo para o trabalho 1

# opcao fazer um programa só, fazendo um ponto no meio pra exibir i resultado

# ideia de OPCODE, zerar um espaço de memoria, lipar as memorias
# gerar um erro e gravar em um arquivo de log em um espaço de memoria





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
        



def MEM_BIN_PARA_MEM_INSTRUCOES():

    with open("instrucoes_txt.txt", "r") as instrucoes:
        
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
        print("contador de programa: ", contador_programa)

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
            #colocar aqui a funcao escrever no arquivo de saida
            with open("output.txt", "w") as txt_file:
                for line in MEM_INTRUCOES:
                    txt_file.write("".join(line) + "\n")
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
    print(contador_programa)
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

    print("DUMP da memoria após sub\n")
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

    print("DUMP da memoria após mult\n")
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

    print("DUMP da memoria após div\n")
    print(MEM_INTRUCOES)

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

def main():
    global contador_programa

    MEM_BIN_PARA_MEM_INSTRUCOES()

    print("DUMP da memoria inicial\n")
    print(MEM_INTRUCOES)

    print("Compilador iniciado")
    LER_INSTRUCAO()


main()

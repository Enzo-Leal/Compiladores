# OP_CODES
OP_SOMA = 10000001
OP_SUB = 10000010
OP_MULT = 10000011
OP_DIV = 10000100
OP_JMP = 10000101
OP_CLEAR_MEM = 10000110
OP_EXIT = 11111111

#Contador de instrucoes
proxima_instrucao = 0

#Array que armazena as instrucoes lidas do arquivo "1_instrucoes.txt"
INSTRUCOES = []

#array de memória de saida totalmente zerado
CODIGO_SAIDA = [00000000,
                00000000,
                00000000,
                00000000,
                00000000,
                00000000,
                00000000,
                00000000,
                00000000,
                00000000,
                00000000,
                00000000,
                00000000,
                00000000,
                00000000,
                00000000,
                00000000,
                00000000,
                00000000,
                00000000,
                00000000,
                00000000,
                00000000,
                00000000,
                00000000,
                00000000,
                00000000,
                00000000,
                00000000,
                00000000,
                00000000,
                00000000,
                00000000,
                00000000,
                00000000,
                00000000,
                00000000,
                00000000,
                00000000,
                00000000,
                00000000,
                00000000,
                00000000,
                00000000,
                00000000,
                00000000,
                00000000,
                00000000,
                00000000,
                00000000,
                00000000,
                00000000,
                00000000,
                00000000,
                00000000,
                00000000,
                00000000,
                00000000,
                00000000,
                00000000,
                00000000,
                00000000,
                00000000,
                00000000,
                00000000]


#função que le as instrucoes e a armazena em um array
def LER_INSTRUCOES():
    with open("1_instrucoes.txt") as f:
        for line in f:
            INSTRUCOES.append(line.strip())


#função que insere os valores do array "CODIGO_SAIDA" no arquivo "3_saida_montador"
def ADICIONAR_ARQUIVO_SAIDA():
    with open("3_saida_montador.txt", "w") as arquivo:
        for line in CODIGO_SAIDA:
            arquivo.write(str(line) + "\n")


def ADC():
    global proxima_instrucao
    proxima_instrucao += 1

    VALOR = int(INSTRUCOES[proxima_instrucao])
    
    proxima_instrucao += 1
    CODIGO_SAIDA[int(INSTRUCOES[proxima_instrucao])] = VALOR


def SUM():
    global proxima_instrucao
    proxima_instrucao += 1
    POS_MEM_INSTRUCAO = int(INSTRUCOES[proxima_instrucao])
    CODIGO_SAIDA[int(POS_MEM_INSTRUCAO)] = int(OP_SOMA)
    
    


def SUB():
    global proxima_instrucao
    proxima_instrucao += 1
    POS_MEM_INSTRUCAO = int(INSTRUCOES[proxima_instrucao])
    CODIGO_SAIDA[int(POS_MEM_INSTRUCAO)] = int(OP_SUB)



def MULT():
    global proxima_instrucao
    proxima_instrucao += 1
    POS_MEM_INSTRUCAO = int(INSTRUCOES[proxima_instrucao])
    CODIGO_SAIDA[int(POS_MEM_INSTRUCAO)] = int(OP_MULT)
    


def DIV():
    global proxima_instrucao
    proxima_instrucao += 1
    POS_MEM_INSTRUCAO = int(INSTRUCOES[proxima_instrucao])
    CODIGO_SAIDA[int(POS_MEM_INSTRUCAO)] = int(OP_DIV)
    


def JMP():
    global proxima_instrucao
    proxima_instrucao += 1
    POS_MEM_INSTRUCAO = int(INSTRUCOES[proxima_instrucao])
    CODIGO_SAIDA[int(POS_MEM_INSTRUCAO)] = int(OP_JMP)
    


def CLEAR_MEM():
    global proxima_instrucao
    proxima_instrucao += 1
    POS_MEM_INSTRUCAO = int(INSTRUCOES[proxima_instrucao])
    CODIGO_SAIDA[int(POS_MEM_INSTRUCAO)] = int(OP_CLEAR_MEM)
    

def EXIT():
    global proxima_instrucao
    proxima_instrucao += 1
    POS_MEM_INSTRUCAO = int(INSTRUCOES[proxima_instrucao])
    CODIGO_SAIDA[int(POS_MEM_INSTRUCAO)] = int(OP_EXIT)

#Funcao que percorre as instrucoes e executa as funcoes nescessarias
def EXECUTAR_INSTRUCOES():
    global proxima_instrucao

    TAMANHO_INSTRUCAO = len(INSTRUCOES)

  # Instruções de controle

    COD_ADC = "ADC"  
    COD_SOMA = "SUM"  
    COD_SUB = "SUB"
    COD_MULT = "MULT"
    COD_DIV = "DIV"
    COD_JMP = "JMP"
    COD_CLEAR = "CLEAR_MEM"
    COD_EXIT = "EXIT"

    while proxima_instrucao <= TAMANHO_INSTRUCAO:
        if INSTRUCOES[proxima_instrucao] == COD_SOMA:
            SUM()
            proxima_instrucao += 1
        elif INSTRUCOES[proxima_instrucao] == COD_SUB:
            SUB()
            proxima_instrucao += 1
        elif INSTRUCOES[proxima_instrucao] == COD_MULT:
            MULT()
            proxima_instrucao += 1
        elif INSTRUCOES[proxima_instrucao] == COD_DIV:
            DIV()
            proxima_instrucao += 1
        elif INSTRUCOES[proxima_instrucao] == COD_JMP:
            JMP()
            proxima_instrucao += 1
        elif INSTRUCOES[proxima_instrucao] == COD_CLEAR:
            CLEAR_MEM()
            proxima_instrucao += 1
        elif INSTRUCOES[proxima_instrucao] == COD_ADC:
            ADC()
            
        elif INSTRUCOES[proxima_instrucao] == COD_EXIT:
            EXIT()
            break

        else:
            proxima_instrucao += 1
            EXECUTAR_INSTRUCOES()
            break


def main():
    print("Iniciando programa")
    LER_INSTRUCOES()
    EXECUTAR_INSTRUCOES()
    ADICIONAR_ARQUIVO_SAIDA()
    print("Programa finalizado")


main()

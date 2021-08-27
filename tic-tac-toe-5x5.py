# importação de biblioteca
import os
from time import sleep

# Cores para utilizar no programa
red   = "\033[1;31m"  
blue  = "\033[1;34m"
cyan  = "\033[1;36m"
green = "\033[0;32m"
reset = "\033[0;0m"
bold    = "\033[;1m"
reverse = "\033[;7m"

# Matriz principal, utilizada no jogo
matriz = [
            [' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ']
            ]

# Função utilizada quando o usuário erra informações. Então ela pergunta se quer ou não continuar
def voltar():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("""
    Voltar para o menu?

    (1) - Sim
            
    (2) - Nao

    """)
    voltar = input(" ")
    # Voltar para o menu
    if voltar == "1":
        sleep(2)
        os.system('cls' if os.name == 'nt' else 'clear')
        return main()
    # Voltar a inserir dos jogadores
    if voltar == "2":
        sleep(2)
        os.system('cls' if os.name == 'nt' else 'clear')
        return jogo()
    # Se colocar outro número, o programa vai voltar para o menu
    if voltar != "1" or voltar != "2":
        print(red+"Não existe essa opção"+reset)
        sleep(2)
        os.system('cls' if os.name == 'nt' else 'clear')
        print(red+"Voltando para o menu"+reset)
        sleep(2)
        os.system('cls' if os.name == 'nt' else 'clear')
        return voltar()

#Função para a criação da matriz do tabuleiro
def tabuleiro():
    # Tabuleiro 5x5
    tabuleiro = """
        0   1   2   3   4
    --+-------------------+--
    0 | {} | {} | {} | {} | {} | 0
    --+---+---+---+---+---+--
    1 | {} | {} | {} | {} | {} | 1
    --+---+---+---+---+---+--
    2 | {} | {} | {} | {} | {} | 2
    --+---+---+---+---+---+--
    3 | {} | {} | {} | {} | {} | 3
    --+---+---+---+---+---+--
    4 | {} | {} | {} | {} | {} | 4
    --+-------------------+--
    """.format(
    matriz[0][0], matriz[0][1], matriz[0][2], matriz[0][3], matriz[0][4],
    matriz[1][0], matriz[1][1], matriz[1][2], matriz[1][3], matriz[1][4], 
    matriz[2][0], matriz[2][1], matriz[2][2], matriz[2][3], matriz[2][4], 
    matriz[3][0], matriz[3][1], matriz[3][2], matriz[3][3], matriz[3][4], 
    matriz[4][0], matriz[4][1], matriz[4][2], matriz[4][3], matriz[4][4],
    )

    print(tabuleiro)

# Função do jogo
def jogo():
    # Colocar os simbolos global
    global nomesimboloX
    global nomesimboloO
    nome1 = input("Digite o nome do primeiro jogador: ")
    # Se o jogador já estiver sido criado, a condição irá continuar o programa
    if os.path.isfile("./usuarios/%s.txt" %nome1):
        sleep(2)
        nome2 = input("Digite o nome do segundo jogador: ")
        # Se o usuário colocar o mesmo nome, o programa irá barrar e perguntar se quer ou não voltar para o menu
        if nome2 == nome1:
            print(red+"Esse jogador já foi escolhido."+reset)
            sleep(2)
            voltar()
        # Se o jogador 2 já estiver sido criado, a condição irá continuar o programa
        if os.path.isfile("./usuarios/%s.txt" %nome2):
            # Pergunta para o primeiro jogador qual simbolo ele gostaria de usar
            print("%s escolha seu simbolo entre X e O: "% nome1)
            simbolo1 = input(" ")
            # Se o simbolo escolhido for correto, ele irá continuar o programa
            if simbolo1 == "X" or simbolo1 == "x":
                simbolo1 = "X"
                nomesimboloX = nome1
                nomesimboloO = nome2
                simbolo2 = "O"
                # Se o simbolo escolhido for [X], o jogador 1 irá ficar com [X] e o jogador 2 com [O]
                print("%s ficará com [X]"%(nome1))
                print("%s ficará com [O]"%(nome2))
                jogadas = 0
                tabuleiro()
                # Repetição para inserir simbolos no tabuleiro (no caso são 12 vezes = 12 "X" + 12 "O" = 24 | o ultimo fica fora da repetição)
                while jogadas < 12:
                    print(blue+"%s sua vez de jogar!"%(nome1)+reset)
                    # Perguntar o lugar onde irá ser inserido o simbolo 
                    linha = int(input("Digite a linha: "))
                    coluna = int(input("Digite a coluna: "))
                    # Adicionar o simbolo "X" no tabuleiro
                    matriz[linha][coluna] = simbolo1
                    os.system('cls' if os.name == 'nt' else 'clear')
                    # Printar tabuleiro
                    tabuleiro()
                    # Verificação de vitória para o jogador com o simbolo "X"
                    vitoriax()
                    # Perguntar o lugar onde irá ser inserido o simbolo 
                    print(blue+"%s sua vez de jogar!"%(nome2)+reset)
                    linha = int(input("Digite a linha: "))
                    coluna = int(input("Digite a coluna: "))
                    # Adicionar o simbolo "O" no tabuleiro
                    matriz[linha][coluna] = simbolo2
                    jogadas += 1
                    os.system('cls' if os.name == 'nt' else 'clear')
                    # Printar tabuleiro
                    tabuleiro()
                    # Verificação de vitória para o jogador com o simbolo "O"
                    vitoriao() 
                # Perguntar o lugar onde irá ser inserido o simbolo
                print(blue+"%s sua vez de jogar!"%(nome1)+reset)
                linha = int(input("Digite a linha: "))
                coluna = int(input("Digite a coluna: "))
                # Adicionar o simbolo "X" no tabuleiro
                matriz[linha][coluna] = simbolo1
                # Printar tabuleiro
                tabuleiro()
                # Verificação de vitória para o jogador com o simbolo "X"
                vitoriax()
                sleep(2)
                os.system('cls' if os.name == 'nt' else 'clear')
                # Se não houver vitória, vai dar velha! (empate)
                print(red+"Deu velha!!"+reset)
                sleep(2)
                print("Ambos continuam com a mesma pontuação! Retornando ao menu.")
                sleep(2)
                # Função para voltar ao menu e resetar o tabuleiro
                resetreturn()
            elif simbolo1 == "O" or simbolo1 == "o":
                simbolo1 = "O"
                nomesimboloO = nome1
                nomesimboloX = nome2
                simbolo2 = "X"
                # Se o simbolo escolhido for [O], o jogador 1 irá ficar com [O] e o jogador 2 com [X]
                print("%s ficará com [O]"%(nome1))
                print("%s ficará com [X]"%(nome2))
                jogadas = 0
                tabuleiro()
                # Repetição para inserir simbolos no tabuleiro (no caso são 12 vezes = 12 "X" + 12 "O" = 24 | o ultimo fica fora da repetição)
                while jogadas < 12:
                    # Perguntar o lugar onde irá ser inserido o simbolo
                    print(blue+"%s sua vez de jogar!"%(nome1)+reset)
                    linha = int(input("Digite a linha: "))
                    coluna = int(input("Digite a coluna: "))
                    # Adicionar o simbolo "O" no tabuleiro
                    matriz[linha][coluna] = simbolo1
                    os.system('cls' if os.name == 'nt' else 'clear')
                    tabuleiro()
                    # Verificação de vitória para o jogador com o simbolo "O"
                    vitoriao()
                    # Perguntar o lugar onde irá ser inserido o simbolo
                    print(blue+"%s sua vez de jogar!"%(nome2)+reset)
                    linha = int(input("Digite a linha: "))
                    coluna = int(input("Digite a coluna: "))
                    # Adicionar o simbolo "X" no tabuleiro
                    matriz[linha][coluna] = simbolo2
                    jogadas += 1
                    os.system('cls' if os.name == 'nt' else 'clear')
                    # Printar tabuleiro
                    tabuleiro()
                    # Verificação de vitória para o jogador com o simbolo "X"
                    vitoriax()
                # Perguntar o lugar onde irá ser inserido o simbolo
                print(blue+"%s sua vez de jogar!"%(nome1)+reset)
                linha = int(input("Digite a linha: "))
                coluna = int(input("Digite a coluna: "))
                # Adicionar o simbolo "O" no tabuleiro
                matriz[linha][coluna] = simbolo1
                # Printar tabuleiro
                tabuleiro()
                # Verificação de vitória para o jogador com o simbolo "O"
                vitoriao()
                sleep(2)
                os.system('cls' if os.name == 'nt' else 'clear')
                # Se não houver vitória, vai dar velha! (empate)
                print(red+"Deu velha!!"+reset)
                sleep(2)
                print("Ambos continuam com a mesma pontuação!")
                sleep(2)
                # Função para voltar ao menu e resetar o tabuleiro
                resetreturn()
            else:
                print(red+"Esse simbolo não pode ser usado, por favor digite o simbolo certo."+reset)
                return jogo()
        # Se não existir o jogador 2, a condição irá barrar a continuidade do jogo
        else:
            print(red+"Esse jogador não existe"+reset)
            sleep(2)
            voltar()
    # Se não existir o jogador, a condição irá barrar a continuidade do jogo
    else:
        print(red+"Esse jogador não existe"+reset)
        sleep(2)
        voltar()

# Função para resetar o tabuleiro(matriz)
def resetgame():
    for x in range(5):
        for y in range(5):
            matriz[x][y] = " "

# Função para voltar ao menu quando dá velha
def resetreturn():
    os.system('cls' if os.name == 'nt' else 'clear')
    resetgame()
    print("Retornando ao menu")
    sleep(2)
    return main()

# Função para resetar o jogo e dar pontuação (Se o "X" ganhar)
def resetreturnx():
    os.system('cls' if os.name == 'nt' else 'clear')
    # Resetar tabuleiro
    resetgame()
    print(green+"Parábens %s, você ganhou o jogo!"%(nomesimboloX)+reset)
    print(red+"Que pena %s, você perdeu o jogo!"%(nomesimboloO)+reset)
    # abrir arquivo
    arquivo = open("./usuarios/%s.txt"%nomesimboloX, "r")
    # ler arquivo
    historico = arquivo.readlines()
    arquivo.close()
    # Adicionar + 1 ao vencedor
    vitorias = int(historico[0]) + 1
    derrotas = int(historico[1])
    # Abrir arquivo para escrever
    arquivo = open("./usuarios/%s.txt"%nomesimboloX, "w")
    # Escrever no arquivo
    arquivo.write("{0}\n{1}".format(vitorias, derrotas))
    arquivo.close()
    # Abrir arquivo
    arquivo = open("./usuarios/%s.txt"%nomesimboloO, "r")
    # Ler arquivo
    historico = arquivo.readlines()
    arquivo.close()
    # Adicionar + 1 ao perdedor
    vitorias = int(historico[0])
    derrotas = int(historico[1]) + 1
    # Abrir arquivo para escrever
    arquivo = open("./usuarios/%s.txt"%nomesimboloO, "w")
    # Escrever no arquivo
    arquivo.write("{0}\n{1}".format(vitorias, derrotas))
    arquivo.close()
    print("Retornando ao menu")
    sleep(3)
    os.system('cls' if os.name == 'nt' else 'clear')
    # Retornar ao menu
    return main()

# Função para resetar o jogo e dar pontuação (Se o "O" ganhar)
def resetreturno():
    os.system('cls' if os.name == 'nt' else 'clear')
    # Resetar tabuleiro
    resetgame()
    print(green+"Parábens %s, você ganhou o jogo!"%(nomesimboloO)+reset)
    print(red+"Que pena %s, você perdeu o jogo!"%(nomesimboloX)+reset)
    # abrir arquivo
    arquivo = open("./usuarios/%s.txt"%nomesimboloO, "r")
    # Ler arquivo
    historico = arquivo.readlines()
    # Adicionar + 1 ao vencedor
    arquivo.close()
    vitorias = int(historico[0]) + 1
    derrotas = int(historico[1])
    # Abrir arquivo para escrever
    arquivo = open("./usuarios/%s.txt"%nomesimboloO, "w")
    # Escrever no arquivo
    arquivo.write("{0}\n{1}".format(vitorias, derrotas))
    arquivo.close()
    # abrir arquivo
    arquivo = open("./usuarios/%s.txt"%nomesimboloX, "r")
    # Ler arquivo
    historico = arquivo.readlines()
    arquivo.close()
    # Adicionar + 1 ao perdedor
    vitorias = int(historico[0])
    derrotas = int(historico[1]) + 1
    # Abrir arquivo para escrever
    arquivo = open("./usuarios/%s.txt"%nomesimboloX, "w")
    # Escrever no arquivo
    arquivo.write("{0}\n{1}".format(vitorias, derrotas))
    arquivo.close()
    print("Retornando ao menu")
    sleep(2)
    os.system('cls' if os.name == 'nt' else 'clear')
    # Retornar ao menu
    return main()

def vitoriax():
    # De cima para baixo
    if matriz[0][0] == "X" and matriz[1][0] == "X" and matriz[2][0] == "X" and matriz[3][0] == "X":
        resetreturnx()
    elif matriz[0][1] == "X" and matriz[1][1] == "X" and matriz[2][1] == "X" and matriz[3][1] == "X":
        resetreturnx() 
    elif matriz[0][2] == "X" and matriz[1][2] == "X" and matriz[2][2] == "X" and matriz[3][2] == "X":
        resetreturnx()
    elif matriz[0][3] == "X" and matriz[1][3] == "X" and matriz[2][3] == "X" and matriz[3][3] == "X":
        resetreturnx()
    elif matriz[0][4] == "X" and matriz[1][4] == "X" and matriz[2][4] == "X" and matriz[3][4] == "X":
        resetreturnx()
    # De baixo para cima
    elif matriz[1][0] == "X" and matriz[2][0] == "X" and matriz[3][0] == "X" and matriz[4][0] == "X":
        resetreturnx()
    elif matriz[1][1] == "X" and matriz[2][1] == "X" and matriz[3][1] == "X" and matriz[4][1] == "X":
        resetreturnx()
    elif matriz[1][2] == "X" and matriz[2][2] == "X" and matriz[3][2] == "X" and matriz[4][2] == "X":
        resetreturnx()
    elif matriz[1][3] == "X" and matriz[2][3] == "X" and matriz[3][3] == "X" and matriz[4][3] == "X":
        resetreturnx()
    elif matriz[1][4] == "X" and matriz[2][4] == "X" and matriz[3][4] == "X" and matriz[4][4] == "X":
        resetreturnx()
    # Da esquerda para direita
    elif matriz[0][0] == "X" and matriz[0][1] == "X" and matriz[0][2] == "X" and matriz[0][3] == "X":
        resetreturnx()
    elif matriz[1][0] == "X" and matriz[1][1] == "X" and matriz[1][2] == "X" and matriz[1][3] == "X":
        resetreturnx()
    elif matriz[2][0] == "X" and matriz[2][1] == "X" and matriz[2][2] == "X" and matriz[2][3] == "X":
        resetreturnx()
    elif matriz[3][0] == "X" and matriz[3][1] == "X" and matriz[3][2] == "X" and matriz[3][3] == "X":
        resetreturnx()
    elif matriz[4][0] == "X" and matriz[4][1] == "X" and matriz[4][2] == "X" and matriz[4][3] == "X":
        resetreturnx()
    # Da direita para a esquerda
    elif matriz[0][1] == "X" and matriz[0][2] == "X" and matriz[0][3] == "X" and matriz[0][4] == "X":
        resetreturnx()
    elif matriz[1][1] == "X" and matriz[1][2] == "X" and matriz[1][3] == "X" and matriz[1][4] == "X":
        resetreturnx()
    elif matriz[2][1] == "X" and matriz[2][2] == "X" and matriz[2][3] == "X" and matriz[2][4] == "X":
        resetreturnx()
    elif matriz[3][1] == "X" and matriz[3][2] == "X" and matriz[3][3] == "X" and matriz[3][4] == "X":
        resetreturnx()
    elif matriz[4][1] == "X" and matriz[4][2] == "X" and matriz[4][3] == "X" and matriz[4][4] == "X":
        resetreturnx()
    # Diagonal principal
    elif matriz[0][0] == "X" and matriz[1][1] == "X" and matriz[2][2] == "X" and matriz[3][3] == "X":
        resetreturnx()
    elif matriz[1][1] == "X" and matriz[2][2] == "X" and matriz[3][3] == "X" and matriz[4][4] == "X":
        resetreturnx()
    elif matriz[1][0] == "X" and matriz[2][1] == "X" and matriz[3][2] == "X" and matriz[4][3] == "X":
        resetreturnx()
    elif matriz[0][1] == "X" and matriz[1][2] == "X" and matriz[2][3] == "X" and matriz[3][4] == "X":
        resetreturnx()
    # Diagonal secundaria
    elif matriz[4][0] == "X" and matriz[3][1] == "X" and matriz[2][2] == "X" and matriz[1][3] == "X":
        resetreturnx()
    elif matriz[3][1] == "X" and matriz[2][2] == "X" and matriz[1][3] == "X" and matriz[0][4] == "X":
        resetreturnx()
    elif matriz[3][0] == "X" and matriz[2][1] == "X" and matriz[1][2] == "X" and matriz[0][3] == "X":
        resetreturnx()
    elif matriz[4][1] == "X" and matriz[3][2] == "X" and matriz[2][3] == "X" and matriz[1][4] == "X":
        resetreturnx()

def vitoriao():
    # De cima para baixo
    if matriz[0][0] == "O" and matriz[1][0] == "O" and matriz[2][0] == "O" and matriz[3][0] == "O":
        resetreturno()
    elif matriz[0][1] == "O" and matriz[1][1] == "O" and matriz[2][1] == "O" and matriz[3][1] == "O":
        resetreturno() 
    elif matriz[0][2] == "O" and matriz[1][2] == "O" and matriz[2][2] == "O" and matriz[3][2] == "O":
        resetreturno()
    elif matriz[0][3] == "O" and matriz[1][3] == "O" and matriz[2][3] == "O" and matriz[3][3] == "O":
        resetreturno()
    elif matriz[0][4] == "O" and matriz[1][4] == "O" and matriz[2][4] == "O" and matriz[3][4] == "O":
        resetreturno()
    # De baixo para cima
    elif matriz[1][0] == "O" and matriz[0][2] == "O" and matriz[3][0] == "O" and matriz[4][0] == "O":
        resetreturno()
    elif matriz[1][1] == "O" and matriz[2][1] == "O" and matriz[3][1] == "O" and matriz[4][1] == "O":
        resetreturno()
    elif matriz[1][2] == "O" and matriz[2][2] == "O" and matriz[3][2] == "O" and matriz[4][2] == "O":
        resetreturno()
    elif matriz[1][3] == "O" and matriz[2][3] == "O" and matriz[3][3] == "O" and matriz[4][3] == "O":
        resetreturno()
    elif matriz[1][4] == "O" and matriz[2][4] == "O" and matriz[3][4] == "O" and matriz[4][4] == "O":
        resetreturno()
    # Da esquerda para direita
    elif matriz[0][0] == "O" and matriz[0][1] == "O" and matriz[0][2] == "O" and matriz[0][3] == "O":
        resetreturno()
    elif matriz[1][0] == "O" and matriz[1][1] == "O" and matriz[1][2] == "O" and matriz[1][3] == "O":
        resetreturno()
    elif matriz[2][0] == "O" and matriz[2][1] == "O" and matriz[2][2] == "O" and matriz[2][3] == "O":
        resetreturno()
    elif matriz[3][0] == "O" and matriz[3][1] == "O" and matriz[3][2] == "O" and matriz[3][3] == "O":
        resetreturno()
    elif matriz[4][0] == "O" and matriz[4][1] == "O" and matriz[4][2] == "O" and matriz[4][3] == "O":
        resetreturno()
    # Da direita para a esquerda
    elif matriz[0][1] == "O" and matriz[0][2] == "O" and matriz[0][3] == "O" and matriz[0][4] == "O":
        resetreturno()
    elif matriz[1][1] == "O" and matriz[1][2] == "O" and matriz[1][3] == "O" and matriz[1][4] == "O":
        resetreturno()
    elif matriz[2][1] == "O" and matriz[2][2] == "O" and matriz[2][3] == "O" and matriz[2][4] == "O":
        resetreturno()
    elif matriz[3][1] == "O" and matriz[3][2] == "O" and matriz[3][3] == "O" and matriz[3][4] == "O":
        resetreturno()
    elif matriz[4][1] == "O" and matriz[4][2] == "O" and matriz[4][3] == "O" and matriz[4][4] == "O":
        resetreturno()
    # Diagonal principal
    elif matriz[0][0] == "O" and matriz[1][1] == "O" and matriz[2][2] == "O" and matriz[3][3] == "O":
        resetreturno()
    elif matriz[1][1] == "O" and matriz[2][2] == "O" and matriz[3][3] == "O" and matriz[4][4] == "O":
        resetreturno()
    elif matriz[1][0] == "O" and matriz[2][1] == "O" and matriz[3][2] == "O" and matriz[4][3] == "O":
        resetreturno()
    elif matriz[0][1] == "O" and matriz[1][2] == "O" and matriz[2][3] == "O" and matriz[3][4] == "O":
        resetreturno()
    # Diagonal secundaria
    elif matriz[4][0] == "O" and matriz[3][1] == "O" and matriz[2][2] == "O" and matriz[1][3] == "O":
        resetreturno()
    elif matriz[3][1] == "O" and matriz[2][2] == "O" and matriz[1][3] == "O" and matriz[0][4] == "O":
        resetreturno()
    elif matriz[3][0] == "O" and matriz[2][1] == "O" and matriz[1][2] == "O" and matriz[0][3] == "O":
        resetreturno()
    elif matriz[4][1] == "O" and matriz[3][2] == "O" and matriz[2][3] == "O" and matriz[1][4] == "O":
        resetreturno()

# Função para criar um novo jogador
def criarjogador():
    # Criar um novo arquivo .txt com o nome do jogador e suas informações
    nome = input("Digite o nome do jogador: ")
    # Se o nome do jogador já estiver sido criado, a condição barra a criação de um novo arquivo
    if os.path.isfile("./usuarios/%s.txt"% nome):
        print(red+"Jogador já registrado"+reset)
        sleep(2)
        os.system('cls' if os.name == 'nt' else 'clear')
    # Se o nome do jogador não estiver sido criado, a condição continua a criação do arquivo
    else:
        # Arquivo será salvo em ./usuarios/nome_do_jogador.txt
        arquivo = open("./usuarios/%s.txt"% nome, "w")
        arquivo.write("0\n")
        arquivo.write("0")
        arquivo.close()
        print(green+"Jogador criado com sucesso!"+reset)
        sleep(2)
        os.system('cls' if os.name == 'nt' else 'clear')

# Função para verificar o histórico dos jogadores
def exibirhistorico():
    nome = input("Digite o nome do jogador: ")
    # Se existir o nome do jogador, a codição continua a verificação do histórico
    if os.path.isfile("./usuarios/%s.txt" %nome):
        os.system('cls' if os.name == 'nt' else 'clear')
        arquivo = open("./usuarios/%s.txt" %nome, "r")
        historico = arquivo.readlines()
        arquivo.close()
        vitorias = int(historico[0])
        derrotas = int(historico[1])
        arquivo = open("./usuarios/%s.txt" %nome, "r")
        print("||*-----------------------------------*||")
        print()
        print(blue+"Jogador: %s"%nome)
        print()
        print(green+"Vitórias: %d"% (vitorias)+reset)
        print(red+"Derrotas: %d"% (derrotas)+reset)
        print()
        print("||*-----------------------------------*||")
        print()
        print()
        arquivo.close()
        print("""
        O que deseja fazer?

        (1) - Exibir outro histórico

        (2) - Voltar para o menu
        """)
        escolhahist = input("")
        # Volta para o começo da função
        if escolhahist == "1":
            sleep(2)
            os.system('cls' if os.name == 'nt' else 'clear')
            return exibirhistorico()
        # Volta para o menu
        if escolhahist == "2":
            sleep(2)
            os.system('cls' if os.name == 'nt' else 'clear')

    # Se não existir o nome do jogador, a condição barra a função e volta para o menu
    else:
        print(red+"Esse jogador não existe"+reset)
        sleep(2)
        os.system('cls' if os.name == 'nt' else 'clear')


# Função para excluir arquivos de jogadores já existentes
def excluirjogador():
    nome = input("Digite o nome do jogador a ser excluido: ")
    # Se existe o nome do jogador, a condição deletará o nome de usuário
    if os.path.isfile("./usuarios/%s.txt"%nome):
        os.remove("./usuarios/%s.txt" %nome)
        print(green+"Jogador excluido com sucesso!"+reset)
        sleep(2)
        os.system('cls' if os.name == 'nt' else 'clear')
    # Se não existir o nome, a condição barra a função e volta para o menu
    else:
        print(red+"Esse jogador não existe!"+reset)
        sleep(2)
        os.system('cls' if os.name == 'nt' else 'clear')

def main():
    # Repetição do menu
    while True:
        print(bold+"""
        ||*---------------- menu ----------------*||

        (1) - Criar novo jogador

        (2) - Exibir histórico de um jogador

        (3) - Excluir jogador

        (4) - Jogar!

        (5) - Sair

        """+reset)
        escolha = input("Digite o número da opção escolhida: ")
        sleep(2)
        os.system('cls' if os.name == 'nt' else 'clear')
        # Condição para a escolha da função desejada
        # Criar jogador
        if escolha == "1":
            criarjogador()
        # Exibir jogador
        elif escolha == "2":
            exibirhistorico()
        # Excluir jogador
        elif escolha == "3":
            excluirjogador()
        # Jogar
        elif escolha == "4":
            jogo()
        # Parar o programa
        elif escolha == "5":
            break
        else:
            print(red+"Por favor escolha um número entre 1 a 5"+reset)
            sleep(2)
            os.system('cls' if os.name == 'nt' else 'clear')


main()

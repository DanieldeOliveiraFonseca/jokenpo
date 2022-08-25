
import random


escolhaJogador = 0
valid = False
jogar_novamente = False


# pedra => 1, papel => 2, tesoura => 3.
def select1():
    if escolhaJogador == 1 and escolhaMaquina == 3:
        print("Você GANHOU \O/ ")
    elif escolhaJogador == 1 and escolhaMaquina == 2:
        print("Você PERDEU :( ")
    elif escolhaJogador == 1 and escolhaMaquina == 1:
        print("EMPATOU. jogue novamente")
    else:
        print("ERRO. informe ao desenvolvedor.")


def select2():
    if escolhaJogador == 2 and escolhaMaquina == 1:
        print("Você GANHOU \O/ ")
    elif escolhaJogador == 2 and escolhaMaquina == 3:
        print("Você PERDEU :( ")
    elif escolhaJogador == 2 and escolhaMaquina == 2:
        print("EMPATOU. jogue novamente")
    else:
        print("ERRO. informe ao desenvolvedor.")


def select3():
    if escolhaJogador == 3 and escolhaMaquina == 2:
        print("Você GANHOU \O/ ")
    elif escolhaJogador == 3 and escolhaMaquina == 1:
        print("Você PERDEU :( ")
    elif escolhaJogador == 3 and escolhaMaquina == 3:
        print("EMPATOU. jogue novamente")
    else:
        print("ERRO. informe ao desenvolvedor.")


print("JOKENPÔ")
print("\n")
print("Escolha PEDRA, PAPEL ou TESOURA.")

while jogar_novamente == False:
    escolhaMaquina = random.randint(1, 3)

    def numeroAleaorio():
        if escolhaMaquina == 1:
            print("Escolha da maquina: PEDRA")
        elif escolhaMaquina == 2:
            print("Escolha da maquina: PAPEL")
        elif escolhaMaquina == 3:
            print("Escolha da maquina: TESOURA")

    while valid == False:
        jogador = input("Sua escolha é: ").lower()

        if jogador == "tesoura":
            escolhaJogador = 3
            valid = True
        elif jogador == "papel":
            escolhaJogador = 2
            valid = True
        elif jogador == "pedra":
            escolhaJogador = 1
            valid = True
        else:
            print("ERRO. Digite apenas PEDRA, PAPEL ou TESOURA.")
            valid = False

        escolhaJogador = escolhaJogador

    numeroAleaorio()

    if escolhaJogador == 1:
        select1()
    elif escolhaJogador == 2:
        select2()
    elif escolhaJogador == 3:
        select3()
    else:
        print("ERRO. Informe ao desenvolvedor.")

    jogarNovamente = input("Deseja jogar novamente? (S ou N) ").lower()
    if jogarNovamente == "n":
        jogar_novamente = True
        sair = input("Precione ENTER para sair.")
    elif jogarNovamente == "s":
        print("--------------------------------------------------------")
        valid = False

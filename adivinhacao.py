import random

def jogar():
    print("*****Bem vindo ao jogo***** ")
    print("***Prepare-se para jogar***")

    num_sec = random.randrange(1,101)

    total_tentativas = 0
    pontos = 0
    print("Qual será a dificuldade do jogo?")
    print("(1) Fácil (2) Médio (3) Díficil\n")

    nivel = int(input("Nível de dificuldade:"))

    if (nivel==1):
        total_tentativas = 20
    elif (nivel==2):
        total_tentativas = 10
    else:
        total_tentativas = 5

    for rodada in range(1,total_tentativas+1):
        print("Tentativa {} de {}".format(rodada, total_tentativas))
        chute=input("Chute um número entre 1 e 100 \n")

        print("Você digitou:\n", chute)
        chute = int(chute)

        if (chute<1 or chute>100):
            print("Somente números entre 1 e 100 \n")
            continue

        certo = num_sec==chute
        maior = num_sec<chute
        menor = num_sec>chute

        if(certo):
             print("Boa escolha. Você acertou!")
             print("Você fez {} pontos \n".format(pontos))
             print("FIM DE JOGO")
             break

        else:
            if(maior):
                print("ERRADO! O seu número é maior do que o número secreto \n")
            elif(menor):
                print("ERRADO! O seu número é menor do que o número secreto \n")

            if (nivel == 1):
                pontos = (total_tentativas - rodada - 1) * 5
            elif (nivel == 2):
                pontos = (total_tentativas - rodada - 1) * 10
            else:
                pontos = (total_tentativas - rodada - 1) * 20

    print("FIM DE JOGO")

if (__name__ == "__main__"):
    jogar()
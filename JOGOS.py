import adivinhacao
import forca

print("*****OLÁ JOGADOR*****")
print("*PRONTO PARA O JOGO?*")
print("*****MUAHAHAHAHA***** \n")
print("(1) para adivinhação ou (2) para forca \n")
jogos = int(input("ESCOLHA O DESAFIO:"))

if jogos == 1:
    print("VOCÊ ESCOLHEU ADIVINHAÇÃO")
    adivinhacao.jogar()
elif jogos == 2:
    print("VOCÊ ESCOLHEU FORCA")
    forca.jogar()

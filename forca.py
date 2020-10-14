import random
# enconding:utf-8

def jogar():

    imprime_apresentação()
    palavra_secreta = cria_palavra_secreta()
    letra_acertada = define_letra_acertada(palavra_secreta)

    print(letra_acertada)

    enforcou = False
    acertou  = False
    erros = 0

    while (not enforcou and not acertou):
        chute = pede_chute()

        if (chute in palavra_secreta):
            marca_chute(chute, letra_acertada, palavra_secreta)
        else:
             erros += 1
             desenha_forca(erros)

        enforcou = erros == 7
        acertou = "_" not in letra_acertada
        print(letra_acertada)

    if(acertou):
        mensagem_vencedor()
    else:
        mensagem_perdedor(palavra_secreta)


def imprime_apresentação():
    print("*****Bem vindo ao jogo da forca******")
    print("********Prepare-se para jogar********")


def cria_palavra_secreta():
    palavras = []
    with open("palavras.txt", "r") as arquivo:
        for linha in arquivo:
            linha = linha.strip()
            palavras.append(linha)
    numero = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero].upper()

    return palavra_secreta

def define_letra_acertada(x):
    return ["_" for letra in x]

def pede_chute():
    chute = input("Chute uma letra:")
    chute = chute.strip().upper()
    return chute

def marca_chute(chute, letra_acertada, palavra_secreta):
    index = 0
    for letra in palavra_secreta:
        if (chute == letra):
            letra_acertada[index] = letra
        index = index + 1

def mensagem_vencedor():
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")

def mensagem_perdedor(palavra_secreta):
    print("Você foi enforcado!")
    print("A palavra secreta era {}".format(palavra_secreta).upper())

def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if erros == 1:
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if erros == 2:
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if erros == 3:
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if erros == 4:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if erros == 5:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if erros == 6:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if erros == 7:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

        print(" |            ")
        print("_|___         ")
        print()

if (__name__ == "__main__"):
        jogar()
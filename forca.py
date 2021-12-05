import random
def jogar():
    print("*"*23)
    print("Bem vindo ao jogo FORCA")
    print("*"*23)
    arquivo = open("palavras.txt","r")
    lista_palavras = []
    num_erros=8

    for linha in arquivo:
        linha = linha.strip() #removi os caracteres especiais
        lista_palavras.append(linha)
    num = random.randint(0,107)

    palavra_secreta = lista_palavras[num]
    palavra_secreta = palavra_secreta.upper()

    ganhou = False
    enforcado = False
    acertos = []
    for letra in palavra_secreta:
        acertos.append("_")
    erros = 0

    print(acertos)
    while not ganhou and not enforcado:

        palpite = input("Digite a letra palpite: ")
        palpite = palpite.upper()
        if palpite in palavra_secreta:
            index = 0
            for letra in palavra_secreta:
                if letra == palpite:
                    acertos[index]= palpite
                index = index+1
        else:
            #erros = erros+1
            erros+=1
        if erros == num_erros:
            enforcado= True
        if "_" not in acertos:
            ganhou = True
        print(acertos)
    if ganhou:
        print("Parabéns, você ganhou!")
    else:
        print("Você perdeu!")
        print(f"A palavra era {palavra_secreta}")

if __name__ == "__main__":
    jogar()
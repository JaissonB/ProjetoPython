import random
def jogar():
    print("*****************************")
    print("Bem vindo ao jogo ADIVINHAÇÃO")
    print("*****************************")

    numero_secreto = random.randint(1,100)
    max_rodadas = 7
    #verificar se ele acertou ou errou

    #se palpite igual numero_secreto
    for rodada in range (1,max_rodadas+1):
        # input permite ler do usuário e retorna uma string (palavra)
        print(f"Rodada {rodada} de {max_rodadas} disponiveis") #print formatado
        palpite = input("Digite o número entre 1 e 100: ")
        palpite = int(palpite)

        if palpite < 1 or palpite > 100:
            print("palpite fora do intervalo (1 e 100)")
            continue
        if palpite == numero_secreto:
            print("Parabéns! Você acertou!")
            break
        else: #caso ele errou
            if palpite < numero_secreto:
                print("Seu palpite foi MENOR que o número secreto!")
            else:
                print("Seu palpite foi MAIOR que o número secreto!")


    print(f"Final do jogo. Você usou {rodada} tentativas")

if __name__ == "__main__":
    jogar()

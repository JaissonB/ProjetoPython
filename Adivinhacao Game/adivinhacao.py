import random

numero_secreto = random.randint(1,100)
rodadas = 6

#verificar se ele acertou ou errou

for rodada in range (1,rodadas+1):
    #input permite ler do usuário e retorna uma string (palavra)
    #print("Rodada ", rodada, " d20:53 28/10/2020 ", rodadas, " disponiveis")
    print(f"Rodada {rodada} de {rodadas} disponiveis")
    palpite = input("Digite o número entre 1 e 100: ")
    palpite = int(palpite)

    if palpite < 1 or palpite > 100:
        print("Palpite fora do intervalo (1 a 100)")
        continue
    if palpite == numero_secreto:
        print("Parabéns! Você acertou!")
        break
    else:
        if palpite < numero_secreto:
            print("Seu palpite foi MENOR que o numero secreto!")
        else:
            print("Seu palpite foi MAIOR que o numero secreto!")

print(f"Final do jogo. Você usou {rodada} tentativas")
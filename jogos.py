import adivinhacao
import forca


print("Escolha o jogo: \n1- para Adivinhação \n2- forca ")

op = input("Escolha o jogo: ")
op = int(op)
if op ==1:
    print("Entrando no jogo Adivinhação...")
    adivinhacao.jogar()

if op ==2:
    print("Entrando no jogo Forca...")
    forca.jogar()
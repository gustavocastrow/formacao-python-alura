import forca
import adivinhacao

def escolher_jogo():
    
    print("Escolha o seu jogo: ")

    print("(1): Forca - (2): Adivinhação")

    jogo = int(input("Qual o jogo? "))

    if(jogo == 1):
        print("Jogando FORCA...")
        forca.jogar()
    elif(jogo == 2):
        print("Jogando ADIVINHAÇÃO...")
        adivinhacao.jogar()

if(__name__ == "__main__"):
    escolher_jogo()
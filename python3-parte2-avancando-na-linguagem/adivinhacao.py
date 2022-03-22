import random

def jogar():
    print("Bem vindo ao jogo de Adivinhação!")

    numero_secreto = random.randint(0, 101)
    total_de_tantativas = 0
    pontos = 1000

    print("Qual nível de dificuldade?", numero_secreto)
    print("(1) Fácil - (2) Médio - (3) Dificíl")

    nivel = int(input("Defina o nível: "))

    if (nivel == 1):
        total_de_tantativas = 20
    elif (nivel == 2):
        total_de_tantativas = 10
    else:
        total_de_tantativas = 5


    for rodada in range(1, total_de_tantativas +1): 
        print(f"Tentativas:{total_de_tantativas}  / Rodada:{rodada}")

        chute_str = input("Digite um número entre 1 e 100: ")
        print(f"Você digitou o número: {chute_str}")

        chute = int(chute_str)

        if (chute < 1 or chute > 100):
            print("Você deve digitar um número entre 1 e 100")
            continue


        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if(acertou):
            print(f"Você acertou e fez {pontos} pontos")
            break
        else:
            if(chute > numero_secreto):
                print("Você errou! o número chutado é MAIOR que o número secreto")
            elif(menor):
                print("Você errou! O número chutado foi MENOR que o número secreto")
            pontos_perdidos = numero_secreto - chute
            pontos = pontos - pontos_perdidos
            
print("Fim de jogo!")

if(__name__ == "__main__"):
    jogar()





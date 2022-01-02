print("Bem vindo ao jogo de Adivinhação!")

numero_secreto = 42
total_de_tantativas = 3

rodada = 1

while(total_de_tantativas > 0):
    print(f"Tentativas:{total_de_tantativas}  / Rodada:{rodada}")
    chute_str = input("Digite o seu número: ")
    print(f"Você digitou o número: {chute_str}")

    chute = int(chute_str)

    acertou = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if(acertou):
        print("Você chutou o número correto!")
    else:
        if(chute > numero_secreto):
            print("Você errou! o número chutado é MAIOR que o número secreto")
        elif(menor):
            print("Você errou! O número chutado foi MENOR que o número secreto")
            
    total_de_tantativas -= 1
    rodada += 1

print("Fim de jogo!")
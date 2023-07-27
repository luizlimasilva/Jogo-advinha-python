print("********************************")
print("bem vindo ao jogo de advinhação!")
print("********************************")



numero_secreto = 42
tentativas = 3

for rodada in range(1, tentativas +1):
    print("Tentativa {} de {}".format(rodada,tentativas))
    chute = int(input("Digite o seu número: "))
    print("Você digitou ", chute)

    if(chute < 1 or chute > 100):
        print("Você deve digitar um número entre 1 e 100!!!")
        continue

    acertou = numero_secreto == chute
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if(acertou):
        print("Você acertou!!!")
        break
    else:
        if(maior):
            print("Você errou! O seu chute foi maior que o número secreto.")
        elif(menor):
            print("Você errou! O seu chute foi menor que o número secreto.")


print("Fim de jogo!!!")
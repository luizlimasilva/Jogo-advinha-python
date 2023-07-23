print("********************************")
print("bem vindo ao jogo de advinhação!")
print("********************************")

numero_secreto = 42

chute = int(input("Digite o seu número: "))

print("Você digitou ", chute)

if(numero_secreto == chute):
    print("Você acertou!!!")
else:
    print("Você errou!")
    print("o número correto é: ", numero_secreto)

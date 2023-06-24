import random

numeros = []

while len(numeros) < 100:
    novo_numero = random.randint(1, 1000)
    if novo_numero not in numeros:
        numeros.append(novo_numero)

print(*numeros, sep='\n')

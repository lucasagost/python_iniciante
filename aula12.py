nome = str(input("Qual é o seu nome? "))
altura = float(input("Qual é sua altura (M)? "))
peso = float(input("Qual é seu peso (KG)? "))
imc = peso / altura ** 2

print(f"{nome} tem {altura} de altura,")
print(f"{peso} KG e seu IMC é: ")
print(round(imc, 2))


"""
nome = 'Luiz Otávio'
altura = 1.80
peso = 95
imc = peso / altura ** 2

print(nome, 'tem', altura, 'de altura,',)
print('pesa', peso, 'quilos e seu imc é',)
print(imc)

# Luiz Otávio tem 1.80 de altura,
# pesa 95 quilos e seu IMC é
# 29.320987654320987
"""

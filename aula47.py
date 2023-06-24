"""
Faça um jogo para o usuário adivinhar qual
a palavra secreta.
- Você vai propor uma palavra secreta
qualquer e vai dar a possibilidade para
o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você 
vai conferir se a letra digitada está
na palavra secreta.
    - Se a letra digitada estiver na
    palavra secreta; exiba a letra;
    - Se a letra digitada não estiver
    na palavra secreta; exiba *.
Faça a contagem de tentativas do seu
usuário.
"""


import random
import os

# Lista de palavras secretas
palavras = ['banana', 'laranja', 'abacaxi', 'limao', 'morango']

# Escolhe uma palavra secreta aleatória
palavra_secreta = random.choice(palavras)

# Cria uma lista com * do mesmo tamanho da palavra secreta
letras_digitadas = ['*' for _ in range(len(palavra_secreta))]

# Contagem de tentativas
tentativas = 0

# Loop do jogo
while True:
    # Limpa a tela do terminal
    os.system('cls' if os.name == 'nt' else 'clear')

    # Exibe a palavra secreta atualizada com as letras acertadas
    print('Palavra secreta:', ''.join(letras_digitadas))

    # Pede ao usuário para digitar uma letra
    letra = input('Digite uma letra: ').lower()

    # Verifica se a letra está na palavra secreta
    acertou = False
    for i, l in enumerate(palavra_secreta):
        if letra == l:
            letras_digitadas[i] = letra
            acertou = True

    # Incrementa a contagem de tentativas
    tentativas += 1

    # Verifica se o usuário acertou todas as letras
    if '*' not in letras_digitadas:
        print('Parabéns, você acertou a palavra secreta "{}" em {} tentativas!'.format(
            palavra_secreta, tentativas))
        break

    # Se o usuário errou a letra, exibe mensagem de erro
    if not acertou:
        print('Letra não encontrada na palavra secreta.')
        print('Tente novamente.')

    input('Pressione ENTER para continuar...')

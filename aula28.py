"""
Exercício
Peça ao usuário para digitar seu nome (ok)
Peça ao usuário para digitar sua idade (ok)
Se nome e idade forem digitados: (ok)
    Exiba:
        Seu nome é {nome} (ok)
        Seu nome invertido é {nome invertido} (ok)
        Seu nome contém (ou não) espaços (ok)
        Seu nome tem {n} letras (ok)
        A primeira letra do seu nome é {letra} (ok)
        A última letra do seu nome é {letra} (ok)
Se nada for digitado em nome ou idade:  (ok)
    exiba "Desculpe, você deixou campos vazios." (ok)
"""
nome = input("Digite seu nome: ")
idade = input("Digite sua idade: ")
nome_invertido = nome[::-1]
num_letras = len(nome)
primeira_letra = nome[0]
ultima_letra = nome[-1]

if len(nome) == 0 or len(idade) == 0:
    print("Desculpe, você deixou campos vazios")
else:
    print(f"Seu nome é {nome}.")
    print(f"Seu nome invertido é {nome_invertido}")
    if ' ' in nome:
        print("Seu nome tem espaços.")
    else:
        print("Seu nome não contém espaços.")
    print(f"Seu nome tem {num_letras} letras.")
    print(f"A primeira letra do seu nome é {primeira_letra}.")
    print(f"A última letra do seu nome é {ultima_letra}.")


"""nome = input('Digite o seu nome: ')
idade = input('Digite sua idade: ')

if nome and idade:
    print(f'Seu nome é {nome}')
    print(f'Seu nome invertido é {nome[::-1]}')

    if ' ' in nome:
        print('Seu nome contém espaços')
    else:
        print('Seu nome NÃO contém espaços')

    print(f'Seu nome tem {len(nome)} letras')
    print(f'A primeira letra do seu nome é {nome[0]}')
    print(f'A última letra do seu nome é {nome[-1]}')
else:
    print("Desculpe, você deixou campos vazios.")"""

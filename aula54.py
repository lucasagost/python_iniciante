"""
Faça uma lista de comprar com listas
O usuário deve ter a possibilidade de
inserir, apagar e listar valores da sua lista
Não permita que o programa quebre com 
erros de índices inexistentes na lista.
"""
import os

lista_compras = []

while True:
    print('--------------------------------------')
    print('          Lista de Compras            ')
    print('                                      ')
    print('[1]Inserir|[2]Apagar|[3]Listar|[0]Sair')
    print('--------------------------------------')
    
    opcao = input('Escolha uma opção: ')

    if opcao == "1":
        os.system('cls')
        item = input('Digite o item a ser inserido: ')
        lista_compras.append(item)
        print(f'{item} inserido na lista de compras!')
        print('--------------------------------------')

    elif opcao == "2":
        os.system('cls')
        if len(lista_compras) == 0:
            print('A lita de compras está vazia!')
        else:
            try:
                indice = int(input('Digite o índice do item a ser removido: '))
                item = lista_compras.pop(indice)
                print(f'{item} foi removido da lista de compras!')
                print('--------------------------------------')
            except (ValueError):
                print('Por favor digite número inteiro!')
                print('--------------------------------------')
            except(IndexError):
                print('Índice não existe na lista!!')
                print('--------------------------------------')
            except(Exception):
                print('Erro desconhecido!')
                print('--------------------------------------')

    elif opcao == "3":
        os.system('cls')
        if len(lista_compras) == 0:
            print("A lista de compras está vázia!")
            print('--------------------------------------')
        else:
            print("Itens na lista de compras: ")
            for i, item in enumerate(lista_compras):
                print(f'{i} - {item}')
            print("Itens na lista de compras: ")

    elif opcao == "0":
        print('Saindo...')
        break
    else:
        print('Opção Inválida. Tente novamente!')


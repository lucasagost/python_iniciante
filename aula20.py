# use if/elif/else
# imputar 2 valor
# comparar - se um valor é maior ele exibido primeiro

primeiro_valor = input('Digite um valor: ')
segundo_valor = input('Digite outro valor: ')

if primeiro_valor > segundo_valor:
    print(
        f"O primeiro valor: {primeiro_valor} é maior que o segundo valor: {segundo_valor}")

elif primeiro_valor == segundo_valor:
    print(
        f"O primeiro valor: {primeiro_valor} é igual o segundo valor: {segundo_valor}")

else:
    print(
        f"O segundo valor: {segundo_valor} é maior que o primeiro: {primeiro_valor}")


"""primeiro_valor = input('Digite um valor: ')
segundo_valor = input('Digite outro valor: ')

if primeiro_valor >= segundo_valor:
    print(
        f'{primeiro_valor=} é maior ou igual '
        f'ao que {segundo_valor=}'
    )
else:
    print(
        f'{segundo_valor=} é maior '
        f'do que {primeiro_valor=}'
    )"""

quantidade_valores = int(input('Digite a quantidade de valores que serão fornecidos para análise: '))
lista = []
for i in range(quantidade_valores):
    valores = int(input('Digite um valor para ser analisado: '))
    lista.append(valores)
    menor_valor = min(lista)
    maior_valor = max(lista)
    media_aritmetica = sum(lista)//quantidade_valores
print(f'Menor valor: {menor_valor}')
print(f'Maior valor: {maior_valor}')
print(f'Média aritmética: {media_aritmetica}')
print('Fim do programa.')
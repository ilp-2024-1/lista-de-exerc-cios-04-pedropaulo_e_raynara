#questão 1
quantidade_par = 0
lista = []
for x in range(10):
    valor = int(input("insira 10 valores:"))
    lista.append (valor)
for item in lista:
    if item%2 == 0 and item !=0:
        quantidade_par += 1
if quantidade_par == 1:
    print(f"você digitou {quantidade_par} valor par.")
else:
    print(f"você digitou {quantidade_par} valores pares.")
print("fim do programa.")

#questão03
pares = 0
lista = []
for i in range(10):
    valores = int(input('Digite um valor inteiro: '))
    lista.append(valores)
    if valores % 2 == 0 and valores != 0:
        pares += 1
print(f'Quantidade de valores par: {pares}')
print('Fim do programa.')

#questão05
quantidade_valores = int(input('Digite a quantidade de valores que serão fornecidos para análise: '))
lista = []
for i in range(quantidade_valores):
    valores = int(input('Digite um valor para ser analisado: '))
    lista.append(valores)
    menor_valor = min(lista)
    maior_valor = max(lista)
    media_aritmetica = sum(lista)/quantidade_valores
print(f'Menor valor: {menor_valor}')
print(f'Maior valor: {maior_valor}')
print(f'Média aritmética: {media_aritmetica}')
print('Fim do programa.')
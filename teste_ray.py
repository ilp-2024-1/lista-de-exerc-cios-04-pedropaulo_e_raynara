pares = 0
lista = []
for i in range(10):
    valores = int(input('Digite 10 valores inteiros: '))
    lista.append(valores)
    if i % 2 == 0:
        pares += 1
print(f'Quantidade de valores par: {pares} ')

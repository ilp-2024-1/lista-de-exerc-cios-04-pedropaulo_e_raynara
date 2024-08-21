pares = 0
lista = []
for i in range(10):
    valores = int(input('Digite um valor inteiro: '))
    lista.append(valores)
    if valores % 2 == 0:
        pares += 1
print(f'Quantidade de valores par: {pares} ')
print('Fim do programa.')
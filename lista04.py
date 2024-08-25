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

#questão 2 
lista1 = []
lista2 = []
soma_par1 = 0
soma_impar1 = 0 
soma_par2 = 0 
soma_impar2 = 0
tamanho_lista = int(input("quantos elementos terá cada lista?"))
for x in range(tamanho_lista):
    valores1 = int(input("insira valores da lista 1:"))
    lista1.append(valores1)

print("\n")

for x in range(tamanho_lista):
    valores2 = int(input("insira valores da lista 2:"))
    lista2.append(valores2)

print("\n")

for item in lista1:
    if item%2 == 0:
        soma_par1 += item
    else:
        soma_impar1 += item

for item in lista2:
    if item%2 == 0:
        soma_par2 += item
    else:
        soma_impar2 += item

print(f"a soma dos números pares da lista 1 é {soma_par1}")
print(f"a soma dos números pares da lista 2 é {soma_par2}")
if soma_par1 > soma_par2:
    print("a soma da lista 1 é maior do que a da lista 2")
elif soma_par1 < soma_par2:
    print("a soma da lista 2 é maior do que a da lista 1")
else:
    print("o valor da soma das listas é igual.")

print('\n')

print(f"a soma dos números ímpares da lista 1 é {soma_impar1}")
print(f"a soma dos números ímpares da lista 2 é {soma_impar2}")
if soma_impar1 > soma_impar2:
    print("a soma da lista 1 é maior do que a da lista 2")
elif soma_impar1 < soma_impar2:
    print("a soma da lista 2 é maior do que a da lista 1")
else:
    print("o valor da soma das listas é igual.")
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

#questão04
lista1 = []
lista2 = []
lista_intercalada = []

tamanho_lista = int(input("quanto elementos terá cada lista?"))

for x in range(tamanho_lista):
    valores_lista1 = str(input("insira elementos da lista 1:"))
    lista1.append(valores_lista1)

print("\n")

for x in range(tamanho_lista):
    valores_lista2 = str(input("insira elementos da lista 2:"))
    lista2.append(valores_lista2)

for item in range(tamanho_lista):
    lista_intercalada.append(lista1[item])
    lista_intercalada.append(lista2[item])

print("\n")

print(f"lista 1 = {lista1}")
print(f"lista 2 = {lista2}")
print(f"lista com valores intercalados da lista 1 e 2 = {lista_intercalada} \n")
print("fim do programa.")


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

#questão06 (precisa de uns ajustes)
lista_numeros = []

for x in range(3):
    numeros = int(input("insira 3 números inteiros:"))
    lista_numeros.append(numeros)
texto = str(input("insira uma string com 3 caractéres:"))
if len(texto) != 3:
    print("erro, a quantidade de caracteres da string deve ser 3")
else:
    for item in range(len(lista_numeros)):
        if item%2 != 0:
            lista_numeros[item] = texto[item]
for item in lista_numeros:
    print(item, end=' ')
print("fim do programa")


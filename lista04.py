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

#questão 2 (corrigir depois)
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

for x in range(tamanho_lista):
    valores2 = int(input("insira valores da lista 2:"))
    lista2.append(valores2)

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
if soma_par1 < soma_par2:
    print("a soma da lista 2 é maior do que a da lista 1")
if soma_par1 == soma_par2:
    print("o número de somas da lista é igual ")

print('\n')

print(f"a soma dos números ímpares da lista 1 é {soma_impar1}")
print(f"a soma dos números ímpares da lista 2 é {soma_impar2}")
if soma_impar1 > soma_impar2:
    print("a soma da lista 1 é maior do que a da lista 2")
if soma_impar1 < soma_impar2:
    print("a soma da lista 2 é maior do que a da lista 1")
if soma_impar1 == soma_impar2:
     print("o número de somas da lista é igual ")
print("fim do programa.")

    
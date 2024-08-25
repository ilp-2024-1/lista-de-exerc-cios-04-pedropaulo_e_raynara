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


    



#questão 1
quantidade_par = 0
lista = []
for x in range(3):
    valor = int(input("insira 10 valores:"))
    lista.append (valor)
for item in lista:
    if item%2 == 0:
        quantidade_par += 1
print(f"você digitou {quantidade_par} valores pares.")
print("fim do programa.")

    
linhas = 3
colunas = 3
matriz = []
valores_impares = 0

for i in range(linhas):
    linha = []
    for j in range(colunas):
        valor = int(input(f"Digite o valor para a posição ({i+1}, {j+1}): "))
        linha += [valor]
        if valor % 2 != 0:
            valores_impares += 1 
    matriz += [linha]

for linha in matriz:
    print(linha)
print(f'Quantidade de números ímpares: {valores_impares}')


    



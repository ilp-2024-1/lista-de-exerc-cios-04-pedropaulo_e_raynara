frase = str(input("escreva uma frase:"))

sinais_pontuacao = ".,!?;:()[]}{\"'"
for sinal in sinais_pontuacao:
    frase = frase.replace(sinal, ' ')
palavras = frase.split()
print(palavras)
contagem = {} 
for palavra in palavras:
    if palavra in contagem:
        contagem[palavra] += 1
    else:
        contagem[palavra] = 1
resultado = ""
for palavra, quantidade in contagem.items():
    resultado += f"{palavra}={quantidade}; "

print(resultado)
    




    



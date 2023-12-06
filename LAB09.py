#Ler a entrada completa
Phrase = input().lower()
CountFrequency = {}
#Desconsiderar espaços em brancos, pontuações e numeros
for caracter in Phrase:
    if caracter.isalpha and caracter not in CountFrequency and caracter.ispunctuation == False:
        CountFrequency[caracter] =''

print(CountFrequency)

#Mostrar todas as letras da frase, numero de ocorrencia e frequencia de ocorrencias
#Mostrar frequencia de vogais
#Mostrar frequencia de consoantes

#Ler a entrada completa
Phrase = input().lower()
CountFrequency = {}
#Desconsiderar espaços em brancos, pontuações e numeros
for caracter in Phrase:
    if caracter.isalpha():
        CountFrequency[caracter] =''
# Contar ocorrencias
for element in CountFrequency:
    count = 0
    for caracter in Phrase:
        if caracter == element:
            count += 1
    CountFrequency[element] = count
print(CountFrequency)

# Calcular frequencias

#Mostrar todas as letras da frase, numero de ocorrencia e frequencia de ocorrencias
#Mostrar frequencia de vogais
#Mostrar frequencia de consoantes


# def countletter(letter, word):
#     count = 0
#     for caracter in word:
#         if letter == caracter:
#             count += 1
#     return count

# for caracter in Phrase:
#     if caracter.isalpha():
#         CountFrequency[caracter] = countletter(caracter, Phrase)
# print('com função')
# print(CountFrequency)
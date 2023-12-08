#Ler a entrada completa
Phrase = input().lower()
CountFrequency = {}
PhraseClear =''
#Desconsiderar espaços em brancos, pontuações e numeros
for caracter in Phrase:
    if caracter.isalpha():
        CountFrequency[caracter] =''
        PhraseClear += caracter
# Contar ocorrencias de todoos os elementos
for element in CountFrequency:
    count = 0
    for caracter in Phrase:
        if caracter == element:
            count += 1
    CountFrequency[element] = count
#Contar ocorrencia de vogais
vowels = ['a','e','i','o','u']
contvowels = 0
for letter in Phrase:
    for vowel in vowels:
        if letter == vowel:
            contvowels += 1
consoants = ['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z']
contcons = 0
for letter in Phrase:
    for cons in consoants:
        if letter == cons:
            contcons += 1

# Calcular frequencias
print ("Letra\tOcorrência\tFrequência")
for chave in sorted(CountFrequency):
    frequency = CountFrequency[chave]/len(PhraseClear)
    print('{}\t{}\t\t{:.2f}'.format(chave,CountFrequency[chave],frequency))

print('Frequência de vogais: {:.2f}'.format(contvowels/len(PhraseClear))) #Fraquencia vogais
print('Frequência de consoantes: {:.2f}'.format(contcons/len(PhraseClear))) #Frequencia consoantes


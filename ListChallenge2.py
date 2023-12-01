#Ler a string 
String = input()
#Desconsiderar os espaços brancos
NewString = ''
for i in String:
    if i != ' ':
        NewString += i
    else: 
        pass
#Reverter a string
NewStringReversed = NewString[::-1]
#Verificar se a string é a mesma da esquerda para a direita e da direita até esquerda
if NewString == NewStringReversed:
#Imprimir se "É palíndromo" ou se "Não é palíndromo"
    print('É palíndromo')
else:
    print('Não é palíndromo')
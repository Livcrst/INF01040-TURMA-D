#Armazenar o historico de usp de app
Application = {}
#Ler os dados 
while True:
    #Receber entrada até um espaço em branco ser oferecido 
    app = input()
    if app == '':
        break
    time = int(input())
    #Se já existir o app no dicionario deverá acrescer o tempo
    if app in Application:
        Application[app] += time
    else:
        Application[app] = time 

print('Aplicativo\tTempo de Utilização')
for chave in sorted(Application, key= Application.get, reverse= True):
    print(f'{chave}\t{Application[chave]}')
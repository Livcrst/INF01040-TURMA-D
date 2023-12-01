
#Variables
Month=[]
TempMonth=[]
MeanYearly = 0

'''Program'''

#Salvar entradas
for i in range(12):
    #Ler o nome de cada mês e Ler o valor de médio da temperatura naquele mesmo mês
    month = input()
    temp = float(input())
    #Armazene em duas listas distintas
    Month.append(month)
    TempMonth.append(temp)
#Calcule a média anual 
for i in TempMonth:
    MeanYearly += i
MeanYearly = MeanYearly/len(TempMonth)
print("%.2f"%MeanYearly)
#Remova os meses abaixo da média anual
i = 0
while i < len(TempMonth):
    if TempMonth[i] < MeanYearly:
        TempMonth.pop(i)
        Month.pop(i)
    else:
        i += 1
#Imprimir saida
for i in range(len(TempMonth)):
    print(Month[i],"%.2f"%TempMonth[i])







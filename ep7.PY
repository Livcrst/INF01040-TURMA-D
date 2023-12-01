# Pegar a entrada (string)
Password = input()
# Verficar se tem entre 6 e 20 digitos
if len(Password) >= 6 and len(Password) <= 20:
    Uppercase = 0
    Lowercase = 0
    Digit = 0
# Verfificar se conter numero de maiscula >= 1
# Verfificar se conter numero de maiscula >= 1
# Verficar se contem pelo menos um digito
# Verficar se contem carater repetido
    for caracter in Password:
        if caracter.isupper():
            Uppercase += 1
        if caracter.islower():
            Lowercase += 1
        if caracter.isdigit():
            Digit +=1
    if Uppercase and Lowercase and Digit:
        Count = 0
        index = 0
        while index < len(Password)-1:
            if Password[index] == Password[index+1]:
                Count += 1 
            index += 1
        #     
        if Count >= 1:
            print('Senha fraca')
        else:
                print('Senha forte')
            
    else:
        print('Senha fraca')
else:
    print('Senha fraca')





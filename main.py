numero = input('Vou dobrar o número que voce digitar: ')

try:
    numero_float = float(numero)
    print('STR: ', numero)
    print('Float: ', numero_float)
    print(f'O dobro de {numero} é {numero_float * 2}')
except:
    print('Isso nao é um número')



# if numero.isdigit():                #Isdigit exige que seja digitado apenas números.
#     numero_float = float(numero)
#     print(f'O dobro de {numero} é {numero_float * 2}')
# else:
#     print('Isso não é um número')
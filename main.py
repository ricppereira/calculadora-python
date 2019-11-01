#=========================================================
# Qualidade de Software
# Ricardo Pereira
#=========================================================

import re
expression = 'start'

print('Qualidade de Software - Calculadora')
print('===================================')
print('Insira a expressão a calcular!')
print('Pode ser utilizado, virgula flutuante(ex:0.10), e as operações:')
print('+  (Soma)')
print('-  (Subtração)')
print('*  (Multiplicação)')
print('/  (Divisão)')
print('** (Potencia)')
print('\nq  (Para Terminar)')

while expression != 'q':
    expression= input('\nInserir expressão: ')
    print('= ', eval(expression))
    if (re.match(r"^(\d{1,}(\.\d{1,})?(([-+/]|[*]{1,2})\d{1,}(\.\d{1,})?)+)+$",expression)):
        print('= ', eval(expression))
    elif expression == 'q':
        print('Terminando... ')    
    else:
        print('Expressão inválida!')
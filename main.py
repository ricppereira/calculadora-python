#=========================================================
# Qualidade de Software
# Ricardo Pereira
# 2019/11/1
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
    try:
        if (re.match(r"^(\d{1,}(\.\d{1,})?(([-+/]|[*]{1,2})\d{1,}(\.\d{1,})?)+)+$",expression)):
            print('= ', eval(expression))
        elif expression == 'q':
            print('Terminando... ')    
        else:
            print('Expressão inválida!')
    except:
        print("Aconteceu qualquer situação anómala!")
import calculadora
def menu():
  print('***************************')
  print('1 - Somar')
  print('2 - Subtrair')
  print('3 - Multiplicar')
  print('4 - Dividir')
  print('5 - Potencia')
  print('6 - Raiz quadrada')
  print('7 - Sair')
  print('***************************')
menu()
opcao = eval(input('Digite a opção desejada: '))
while(opcao!=7):
  if (opcao==1):
    x=eval(input('Digite um valor inteiro do primeiro termo da soma:'))
    y=eval(input('Digite um valor inteiro do segundo termo da soma:'))
    print(calculadora.calcula_soma(x,y))
  elif (opcao==2):
    x=eval(input('Digite um valor inteiro do primeiro termo da subtração:'))
    y=eval(input('Digite um valor inteiro do segundo termo da subtração:'))
    print(calculadora.calcula_subtracao(x,y))
  elif (opcao==3):
    x=eval(input('Digite um valor inteiro do primeiro termo da multiplicação:'))
    y=eval(input('Digite um valor inteiro do segundo termo da multiplicação:'))
    print(calculadora.calcula_multiplicacao(x,y))
  elif (opcao==4):
    x=eval(input('Digite um valor inteiro do primeiro termo da divisão:'))
    y=eval(input('Digite um valor inteiro do segundo termo da divisão diferente de 0:'))
    while(y==0):
      x=eval(input('Digite um valor inteiro do primeiro termo da divisão:'))
      y=eval(input('Digite um valor inteiro do segundo termo da divisão diferente de 0:'))
    print(calculadora.calcula_divisao(x,y))
  elif (opcao==5):
    x=eval(input('Digite um valor inteiro do primeiro termo da potencia:'))
    y=eval(input('Digite um valor inteiro do segundo termo da potencia (expoente):'))
    print(calculadora.calcula_potencia(x,y))
  elif (opcao==6):
    x=eval(input('Digite um valor inteiro positivo:'))
    while(x<0):
      x=eval(input('Digite um valor inteiro positivo:'))
    print(calculadora.calcula_raizquadrada(x))
 
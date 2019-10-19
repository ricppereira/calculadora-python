def calcula_soma(x,y):
      soma=x+y
  return soma
def calcula_subtracao(x,y):
  subtracao=x-y
  return subtracao
def calcula_multiplicacao(x,y):
  multiplicacao=x*y
  return multiplicacao
def calcula_divisao(x,y):
  dividir=x/y
  return dividir  
def calcula_potencia(x,y):
  potencia=x**y
  return potencia
def calcula_raizquadrada(x,expoente=2):
  if (x>0):
    raiz=x**(1/expoente)
  else:
    print('O termo precisa ser um numero positivo')
  return raiz
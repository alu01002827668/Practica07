#!/src/bin/python

import modulo

valores=(1e1, 1e2, 1e3, 10000, 100000, 1000000, 10000000, 100000000)
lista = []


for i in valores:
  y=modulo.aproximacion_PI(i)
  lista = lista + [y] 
  print y

#mostrar(lista)
  

# El numero maximo de elemntos es 7
# Para 8 elementos se producen errores
# Se pueden definir los elementos en notacion cientifica
#El archivo .pyc se crea despues de la primera ejecucion del modulo importado, el programa Python utilizara el .pyc compilado al importar
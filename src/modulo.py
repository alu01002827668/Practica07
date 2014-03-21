#!/usr/bin/python
import sys

PI= 3.14155926535897931159979634685441852

def aproximacion_PI(n):
  n = int(n) 
  if(n!=0):
    
    suma = 0.0
    for i in range(1,n+1):
      x_i=(i-0.5)/float(n)
      fx_i=4/(1+x_i*x_i)
      b=i/float(n)
      a = b-(1 / float(n))
      suma=suma+fx_i

    PI_i=suma/float(n)
    return PI_i
  
if __name__ == "__main__":
  
  n = 0
  m = 0
  
  if(len(sys.argv)!=3):
    print 'No se han ingresado los parametros. Se usaran los valores por defecto'
    n=10
    m=10
    
  else:
    n=int(sys.argv[1])
    m=int(sys.argv[2])
  
  lista = []  

  for j in range(1,m+1):
    pi=aproximacion_PI(j*m)
    lista = lista +[pi]
    
  print lista

  for z in range(0, m):
    npi = lista[z]
    dif = pi - npi
    print 'PI35DT : %.35f lista: %f PI35DT-lista: %f ' % (pi,npi,dif)
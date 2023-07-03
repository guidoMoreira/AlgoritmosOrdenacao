import time
import random
import matplotlib.pyplot as plt

def QuickSort(X, inicio, fim):
  i = inicio
  j = fim
  pivo = X[(i+j)//2]
  while i<=j:
    while X[i] < pivo:
      i+=1
    while X[j]>pivo:
      j-=1
    if i<=j:
      aux = X[i]
      X[i] = X[j]
      X[j] = aux
      i+=1
      j-=1
  if inicio < j:
    QuickSort(X,inicio,j)
  if i < fim:
    QuickSort(X,i,fim)
      



ns = [10000, 25000, 50000, 100000, 200000]
MP =[]
MMd =[]
MMl =[]
for j in ns:
  n = j




  
  #PIOR CASO=================
  f = open("Resultado.txt", "a")
  print("Pior Caso:")
  f.write("Pior Caso n = " + str(n) + ":\n")
  m = 0
  for i in range(0, 10):
    A = []
    for i in range(0, n):
      A.append(n - i)

    begin = time.time()
    QuickSort(A, 0, n-1)
    end = time.time()
    m += end - begin
    f.write(str(end - begin) + "\n")
    print(end - begin)
  m /= 10
  MP.append(m)
  f.write("Media: " + str(m) + "\n\n")

  #MELHOR CASO===============
  print("Melhor Caso:")
  f.write("Melhor Caso n = " + str(n) + ":\n")
  m = 0
  for i in range(0, 10):
    A = []
    for i in range(0, n):
      A.append(i)

    begin = time.time()
    QuickSort(A, 0, n-1)
    end = time.time()
    m += end - begin
    f.write(str(end - begin) + "\n")
    print(end - begin)
  m /= 10
  MMl.append(m)
  f.write("Media: " + str(m) + "\n\n")

  #CASO MEDIO==============

  print("Caso Medio:")
  f.write("Caso Medio n = " + str(n) + ":\n")
  m = 0
  for i in range(0, 10):
    A = []
    for i in range(0, n):
      A.append(random.randint(0, n))

    begin = time.time()
    QuickSort(A, 0, n-1)
    end = time.time()
    m += end - begin
    f.write(str(end - begin) + "\n")
    print(end - begin)
  m /= 10
  MMd.append(m)
  f.write("Media: " + str(m) + "\n\n")
f.close()


plt.plot(ns,MP,'r', label="Vetor ordenado decrescente")
plt.plot(ns,MMl,'g', label="Vetor ordenado crescente")
plt.plot(ns,MMd,'b', label="Vetor de valores aleatório")
plt.xlabel('Tamanho n do vetor')
plt.ylabel('Tempo Demorado')
plt.legend()
plt.savefig('mediastemp.png')
plt.show()
plt.close()
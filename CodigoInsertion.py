import time
import random
import matplotlib.pyplot as plt

def InsertionSort(A, n):
  for j in range(1,n):
    chave = A[j]
    i = j-1
    while i >= 0 and A[i] > chave:
      A[i+1] = A[i]
      i = i-1
    A[i+1] = chave
  

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
    InsertionSort(A, n)
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
    InsertionSort(A, n)
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
    InsertionSort(A, n)
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
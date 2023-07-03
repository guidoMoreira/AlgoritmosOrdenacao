import time
import random
import matplotlib.pyplot as plt

def MergeSort(A, inicio, fim):
  if inicio < fim:
    meio = (inicio + fim) // 2
    MergeSort(A, inicio, meio)
    MergeSort(A, meio + 1, fim)
    Combina(A, inicio, meio, fim)


def Combina(A, inicio, meio, fim):
  n1 = meio - inicio + 1
  n2 = fim - meio
  B = []
  C = []
  for i in range(0, n1):
    B.append(A[inicio + i - 1])
  for j in range(0, n2):
    C.append(A[meio + j])
  i = 0
  j = 0
  k = inicio - 1
  while (i < n1 and j < n2):
    if B[i] <= C[j]:
      A[k] = B[i]
      i += 1
    else:
      A[k] = C[j]
      j += 1
    k += 1
  #
  while i < n1:
    A[k] = B[i]
    i += 1
    k += 1
  while j < n2:
    A[k] = C[j]
    j += 1
    k += 1


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
    MergeSort(A, 1, n)
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
    MergeSort(A, 1, n)
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
    MergeSort(A, 1, n)
    end = time.time()
    m += end - begin
    f.write(str(end - begin) + "\n")
    print(end - begin)
  m /= 10
  MMd.append(m)
  f.write("Media: " + str(m) + "\n\n")
f.close()


plt.plot(ns,MP,'r', label="Pior Caso")
plt.plot(ns,MMl,'g', label="Melhor Caso")
plt.plot(ns,MMd,'b', label="Caso Medio")
plt.xlabel('Tamanho n do vetor')
plt.ylabel('Tempo Demorado')
plt.legend()
plt.show()


import time
import random
import matplotlib.pyplot as plt
def countSort(A, pind):
    cA = [0] * 10#contador digitos
    tA = len(A) #tamanho Vetor

    #Conta digitos totais
    for i in range(tA): 
        posD = (A[i] // pind) % 10
        cA[posD] += 1

    #soma com o numero anterior para calcular os novos indices
    for i in range(1, 10):
        cA[i] += cA[i-1]

    #Criar vetor ordenado
    auxv = [0] * tA

    #Ultimo indice do vetor
    i = tA - 1

    #Colocar elemento na posição
    while i >= 0:
        posD = (A[i] // pind) % 10#pega digito do elemento atual
        cA[posD] -= 1 #diminui valor no indice para pegar posição não usada
        posV = cA[posD]#Pega posição atualizada
        auxv[posV] = A[i]#Coloca elemento na posição calculada
        i -= 1#Faz o mesmo pro elemento anterior
    return auxv
def RadixSort(X):
  maxVal = max(X)#pega maior valor
  nD = 1#numero de digitos do maior valor

  #calcula número de digitos do maior elemento
  while maxVal > 0:
      maxVal /= 10
      nD += 1

  #"indice" do digito (unidade, dezena, centena ...)
  ind = 1

  #Cria cópia do vetor para modificar
  aux = X.copy()

  #Realiza a organização contando no indice do digito passado começando na unidade indo até o do maior elemento
  while nD > 0:
    aux = countSort(aux, ind)
    ind *=10#Passa para a proxima unidade
    nD-=1#tira um dos digitos a analisar
  return aux
  


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
    A = RadixSort(A)
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
    A = RadixSort(A)
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
    A = RadixSort(A)
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
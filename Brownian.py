import numpy as np
import matplotlib.pyplot as plt

#Autor: Ivan Grana

np.random.seed(4)
n = 10**5 #quantidade de iteracoes

SQN = 1/np.math.sqrt(n) # Formula de atualização

Z_valores = np.random.randn(n)
Yk = 0
SB_movimento=list()

for k in range(n):
     Yk = Yk + SQN*Z_valores[k] #Função de atualização da posição da particula
     SB_movimento.append(Yk)
  
plt.plot(SB_movimento)
plt.title("Movimento Browniano")
plt.ylabel("Posição Y")
plt.xlabel("Iterações (n)")
plt.show()

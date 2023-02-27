import numpy as np
import matplotlib.pyplot as plt

# Exponential growth model
def exponential_growth(N0, r, t):
    N = N0 * np.exp(r * t)
    return N

# Logistic growth model
def logistic_growth(N0, r, K, t):
    N = K / (1 + ((K - N0) / N0) * np.exp(-r * t))
    return N

# Plotting the population growth curves
t = np.linspace(0, 10, 100) # intervalo de tempo
N0 = 100 # População inicial
r = 0.2 # Taxa de crescimento
K = 1000 # carrying capacity

# Calculate population sizes using exponential and logistic growth models
N_exp = exponential_growth(N0, r, t)
N_log = logistic_growth(N0, r, K, t)

# Plot the population growth curves
plt.plot(t, N_exp, label='Exponential growth')
plt.plot(t, N_log, label='Logistic growth')
plt.xlabel('Time')
plt.ylabel('Population size')
plt.title('Crescimento populacional')
plt.legend()
plt.show()

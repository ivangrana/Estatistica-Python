import random,matplotlib.pyplot as plt
vetor_resultados = []
frequencia = 0

def rolar_dados():
    """Função que simula o lançamento de um dado de 6 lados"""
    return random.randint(1,6)

def gerar_simulacao(frequencia,numero_dado):
    for k in range(1,2000):
        resultado = rolar_dados()
        if resultado == numero_dado:
            frequencia += 1
        vetor_resultados.append(frequencia/k)
        resultado = 0
    return vetor_resultados

def gerar_grafico(numero_dado):
    fig, ax = plt.subplots()
    ax.plot(range(1,2000),gerar_simulacao(frequencia,numero_dado),color = 'red')
    ax.set_xlabel("Nº de experimentos")
    ax.set_ylabel("Probabilidade de cair o número %d" %numero_dado)
    plt.show()
    
gerar_grafico(3)
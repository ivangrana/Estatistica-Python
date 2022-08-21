import numpy as np
import matplotlib.pyplot as plt

def distribuicao_normal():
    '''Função que gera o grafico de uma distribuicao normal'''
    x = np.random.normal(0.0,0.8,size=9*100000)
    fig,ax = plt.subplots()
    ax.hist(x,100)
    ax.set_xlim(-3,3)
    plt.show()
    

def distribuicao_poisson(lambda_param):
    '''Função que gera o grafico de uma distribuicao de Poisson'''
    x = np.random.poisson(lambda_param,10000)
    fig,ax = plt.subplots()
    ax.hist(x,100)
    plt.show()
 
def distribuicao_uniforme():
    '''Função que gera o grafico de uma distribuicao uniforme'''
    x = np.random.uniform(-1,0,1000)
    fig,ax = plt.subplots()
    ax.hist(x,100)
    plt.show()
    
distribuicao_uniforme()
 

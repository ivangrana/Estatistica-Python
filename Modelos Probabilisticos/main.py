import numpy as np
import matplotlib.pyplot as plt

def plotting_normal():
    x = np.random.normal(0.0,0.8,size=9*100000)
    fig,ax = plt.subplots()
    ax.hist(x,100)
    ax.set_xlim(-3,3)
    plt.show()
    

def plotting_poisson(lambda_param):
    x = np.random.poisson(lambda_param,10000)
    fig,ax = plt.subplots()
    ax.hist(x,100)
    plt.show()
 

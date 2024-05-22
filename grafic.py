import Conexao
import matplotlib.pyplot as plt

from time import sleep
import os



def printGrafico():
    array=Conexao.consultar("2024","05","09")
    dados=[]
    for a in array:
        strig=str(a)
        dado=strig[2:len(strig)-3]
        f=float(dado)
        dados.append(f)

    plt.plot(dados)
    plt.show()
    sleep(20)



printGrafico()
# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.


from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd

import Conexao


app = Dash(__name__)

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options
def gerarGrafico():
    array=Conexao.consultar("2024","05","06")
    dados=[]
    for a in array:
        strig=str(a)
        dado=strig[2:len(strig)-3]
        f=float(dado)
        dados.append(f)
    return dados
    

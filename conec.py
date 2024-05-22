import sqlite3
from sqlite3 import Error
import os

def Conectar():
    caminho="C:\\Users\\O Poderoso Chefão\\Documents\\webscraping\\Bd.db"
    con=None
    try: 
       con=sqlite3.connect(caminho)
       print("conectado com sucesso")
    except Error as ex:
        print(ex)
    return con

vcon=Conectar()

def dql(query): #select
    vcon=Conectar()
    c=vcon.cursor()
    c.execute(query)
    res=c.fetchall()
    vcon.close()
    return res

def dml(query): #inserir,update, delete
    try:
       vcon=Conectar()
       c=vcon.cursor()
       c.execute(query)
       vcon.commit()
       vcon.close()
    except Error as ex:
        print(ex)
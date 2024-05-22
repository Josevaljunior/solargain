#instalando conexão mysql
#pip install mysql-connector-python
import mysql.connector as my

conect= my.connect(host="localhost", user="root", password="", database="solar_gain")

regis="2024-04-08 15:07:43 2 kW"

def incerir(ano,mes,dia,hora,geracao, acumulado):
   cursor= conect.cursor()
   sql='INSERT INTO geracao(Ano, Mes, dia, hora, geracao, acumulado) VALUES(%s, %s, %s, %s, %s,%s)'
   valores=(ano, mes, dia, hora, geracao,acumulado)
   cursor.execute(sql, valores)
   conect.commit()

def consultar(ano, mes, dia):
   cursor= conect.cursor()
   sql='SELECT geracao FROM geracao WHERE Ano='+ano+' AND Mes='+mes+' AND dia='+dia+''
   cursor.execute(sql)
   resultado=cursor.fetchall()
   return resultado

def consultarAcumuado(ano, mes, dia):
   cursor= conect.cursor()
   sql='SELECT acumulado FROM geracao WHERE Ano='+ano+' AND Mes='+mes+' AND dia='+dia+''
   cursor.execute(sql)
   resultado=cursor.fetchall()
   return resultado
   

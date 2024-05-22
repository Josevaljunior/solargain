#Biblitotecas para instalar
#pip install selenium

#instalaçõa BeautifulSoup
#pip install beautifulsoup4

#instalação lxml
#pip install lxml

#instalação pandas
#pip install pandas

#instalação do schedule
#pip install schedule

#instalação flask
#pip install flask
from flask import Flask, render_template, request, redirect, url_for
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from time import sleep
from bs4 import BeautifulSoup
import schedule
import datetime
from datetime import date
import EnviarEmail
import Conexao
import grfocd
import json


app=Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')


def coletarDados(login, senha):
    acumulado=0
    options=Options()
    options.headless=True #executar de forma vis ou n
    navegador=webdriver.Firefox(options=options)
    #abrindo o link
    link="https://www.solarweb.com/"
    navegador.get(url=link)
    sleep(1)

    #encontrando o botão que quero clicar pleo Id no html
    buttonAllow=navegador.find_element(by=By.ID,value="CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll")
    #clicando
    buttonAllow.click()
    sleep(1)

    #encontrando o botão que quero clicar pleo Id no html
    buttonLogin=navegador.find_element(by=By.LINK_TEXT,value="LOGIN")
    #clicando
    buttonLogin.click()
    sleep(2)



    #encontrando o elemento que quero preencher no html
    inputUsuario = navegador.find_element(by=By.ID,value="usernameUserInput")
    #preenchendo o campo
    inputUsuario.send_keys(login)
    sleep(1)

    #encontrando o elemento que quero preencher no html
    inputSenha = navegador.find_element(by=By.ID,value="password")
    #preenchendo o campo
    inputSenha.send_keys(senha)
    sleep(1)

    #encontrando o botão que quero clicar pleo Id no html
    buttonLog=navegador.find_element(by=By.ID,value="login-button")
    #clicando
    buttonLog.click()

    sleep(15)
    cont=0

    while True:
        element=navegador.find_element(by=By.XPATH,value="//div[@class=\"js-status-bar-text\"]//span")
        html_content=element.get_attribute('outerHTML')
        
        soup = BeautifulSoup(html_content, 'html.parser')
        dado=soup.get_text() 
        #pegando horario atual da medição
        dataHorario=str(datetime.datetime.now())
        
        #determiando horario para encerramento do programa
        dataHorario.split()
        hora=int(dataHorario[11]+dataHorario[12])
        minuto=int(dataHorario[14]+dataHorario[15])
        #verificando se meu inversor ficou off-line por pelomenos 5 minutos durante o dia 
        if(dado=="Offline" and hora>=6):
            cont=cont+1
            if(cont==30):              
               EnviarEmail.Enviar("",2,"Seu inverosr esta parado por 5 minutos. Horario: "+dataHorario[0:19])
               cont=0    
        print(dado)
        #Guardando dados no txt
        if(not dado =="Offline"):
            d=str(datetime.datetime.now())
            data=d[0:10]
            name=data+".txt"
            print(name)
            with open(name,'a') as arquivo:
                regis=dataHorario[0:19]+" "+dado
                arquivo.write(regis+'\n')
            tam=len(regis)

            if(regis[tam-2]=="k"):
               if(len(regis)==24):
                   geracao=regis[24]
               else:
                   geracao=regis[20:24]
               
            else:
               geracao="0,"+regis[20:24]
            geracao=geracao.replace(",",".")
            acumulado=float(geracao)/360+acumulado
            print(regis)
           

            
            Conexao.incerir(regis[0:4], regis[5:7], regis[8:10], regis[11:19], geracao, str(acumulado))
            dado.split()
            
            print(dado)

        
        #if(hora==17 and minuto>3):
         #   EnviarEmail.Enviar(name,1,"Dados de geração do dia "+name)
         #   calcularAcumulado(regis[0:4],regis[5:7],regis[8:10])
          #  print("dia finalizado")
          #  return 0
        
        
          
       
        
        
    
        
    
        sleep(10)

@app.route('/logar',methods=['GET','POST'])
def logar():
    if request.method == 'POST':
        login=request.form['login']
        senha=request.form['senha']
        print(login)
        print(senha)
        coletarDados(login,senha)
    return render_template('logar.html')

if __name__=='__main__':
    app.run(debug=True)




def calcularAcumulado(ano, mes, dia):
    valoresDIA=Conexao.consultar(ano, mes, dia)

    for valor in valoresDIA:
        print(valor)


       


#schedule.every().day.at("18").do(coletarDados)
#while True:
  #schedule.run_pending()
  #print("Loadind...")
 # sleep(2)

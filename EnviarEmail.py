import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from email.mime.base import MIMEBase
from email import encoders

#S M T P - Simple Mail transfer protocol
#Para criar o servidor e enviar o email
def Enviar(arquivo,tipoEnv, texto):
    #1 - Começar o servido SMTP
    host="smtp.gmail.com"
    port=" 587"
    login="pibicjoseval@gmail.com"
    senha="pibpuibhpusjrtvp"


    server = smtplib.SMTP(host,port)
    server.ehlo()
    server.starttls()

    server.login(login,senha)

    #2 - Contruir o email tipo mime
    corpo=texto
    email_msg=MIMEMultipart()
    email_msg['From'] = login
    email_msg['To']= login
    email_msg['Subject']= "SOLAR GAIN"
    if(tipoEnv==1):
        #Anexando arquivo
        cam_arquivo=arquivo
        attchment = open(cam_arquivo,'rb')
        #codficando em base 64
        att = MIMEBase('application','octec-stram')
        att.set_payload(attchment.read())
        encoders.encode_base64(att)
        #Adicionando o cabeçalhos no tipo anexo de email
        att.add_header('Content-Disposition', f'attachment; filename=2024-03-1.txt')
        #fechando o arquivo
        attchment.close()
        #anexando ao email
        email_msg.attach(att)

    email_msg.attach(MIMEText(corpo,'plain'))
    #3 - Enviar o email tipo mime no SERVIDOR SMTP
    server.sendmail(email_msg['From'],email_msg['To'],email_msg.as_string())
    server.quit()
    links="https://www.youtube.com/watch?v=N97q96BygUg"
    link="https://www.youtube.com/watch?v=umvzsQLZYD4"
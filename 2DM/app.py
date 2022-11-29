#Bibliotecas necessarias, caso não tenha instalado em sua maquina basta executar os comandos (pip install...)

from selenium import webdriver #pip install selenium
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
import time
import emoji
from webdriver_manager.chrome import ChromeDriverManager #pip install webdriver_manager

#Contatos/Grupos - informar o nome(s) de Grupos ou Contatos que serao enviadas as mensagens
contatos = ["Chatbot", "NADA"]

#Mensagem - Mensagem que sera enviada
mensagem = ["⚠️⚠️Oi pessoal! Só passando pra avisar que o treinamento de AWS para a turma de Desenvolvimento de Sistemas do período da manhã vai ter início no dia 05/12/2022. Lembrando que o treinamento prepara os alunos para a realização da prova de certificação AWS Cloud Practitioner.✅ Contamos com a presença de todos!Acessem o link para mais informações: ✅ https://aws.amazon.com/pt/certification/certified-cloud-practitioner/?trk=9cd9d99c-3597-4b9b-b044-5b9213216efc&sc_channel=ps&s_kwcid=AL!4422!3!544685366846!e!!g!!aws%20cloud%20practitioner&ef_id=CjwKCAiApvebBhAvEiwAe7mHSEAB9PQMcpqS2fmT_hIDfP41rsHPVdRlVr1Htjrevqm6NP7jzLQUZBoCl7MQAvD_BwE:G:s&s_kwcid=AL!4422!3!544685366846!e!!g!!aws%20cloud%20practitioner"]

# Midia = imagem, pdf, documento, video ( caminho do arquivo, lembrando que mesmo no windows o caminho deve ser passado com barra invertida */*)
midia = "C:/Users/SENAI/Pictures/Saved Pictures/aws.png"

#Abre o Chrome
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get('https://web.whatsapp.com/')#Abre o site do Whatsapp Web
time.sleep(30)#da um sleep de 15 segundos, tempo para scannear o QRCODE

#Funcao que pesquisa o Contato/Grupo
def cade_contato(contato):
achar_contato = driver.find_element(By.XPATH, '//div[contains(@class, "copyable-text")]')
time.sleep(2)#da um sleep de 2 segundos para pesquisa
achar_contato.click()
achar_contato.send_keys(contato)
achar_contato.send_keys(Keys.ENTER)

#Funcao que envia a mensagem
def enviar_mensagem(mensagens):
for mensagem in mensagens:
enviar_mensagem = driver.find_element(By.XPATH, '//p[contains(@class, "selectable-text copyable-text")]')
enviar_mensagem.click()
time.sleep(3)
enviar_mensagem.send_keys(mensagem)
enviar_mensagem.send_keys(Keys.ENTER)
time.sleep(2)

#Funcao que envia a midia como mensagem
def enviar_midia(midia):
enviar_midia = driver.find_element(By.CSS_SELECTOR,"span[data-icon='clip']").click()
attach = driver.find_element(By.CSS_SELECTOR,"input[type='file']")
attach.send_keys(midia)
time.sleep(3)
send = driver.find_element(By.CSS_SELECTOR,"span[data-icon='send']")
send.click()

#Percorre todos os Contatos/Grupos e envia as mensagens
for contato in contatos:
cade_contato(contato)
enviar_mensagem(mensagem)
enviar_midia(midia)
time.sleep(1)
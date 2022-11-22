import pywhatkit
import keyboard
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager 
from datetime import datetime

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://web.whatsapp.com/')
time.sleep(30)

contatos = ['Chatbot', 'NADA']
mensagem = 'KAVALO'

def buscar_contato(contato):
    campo_pesquisa = driver.find_element("xpath",'//div[contains(@class,"copyable-text selectable-text")]')
    time.sleep(3)
    campo_pesquisa.click()
    campo_pesquisa.send_keys(contato)
    campo_pesquisa.send_keys(Keys.ENTER)
    
    
for contato in contatos:
    buscar_contato(contato)
    enviar_mensagem(mensagem)
   
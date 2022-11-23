from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
import time
from webdriver_manager.chrome import ChromeDriverManager

contatos = ["Chatbot"]
mensagem = ["oi a vida talvez seja um morango"]
midia = "C:/Users/SENAI/Pictures/Saved Pictures/Senai.jpg"

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get('https://web.whatsapp.com/')
time.sleep(30)

def cade_contato(contato):
    achar_contato = driver.find_element(By.XPATH, '//div[contains(@class, "copyable-text")]')
    time.sleep(2)
    achar_contato.click()
    achar_contato.send_keys(contato)
    achar_contato.send_keys(Keys.ENTER)
    
def enviar_mensagem(mensagens):
    for mensagem in mensagens:
        enviar_mensagem = driver.find_element(By.XPATH, '//p[contains(@class, "selectable-text copyable-text")]')
        enviar_mensagem.click()
        time.sleep(3)
        enviar_mensagem.send_keys(mensagem)
        enviar_mensagem.send_keys(Keys.ENTER)
        time.sleep(2)

def enviar_midia(midia):
    enviar_midia = driver.find_element(By.CSS_SELECTOR,"span[data-icon='clip']").click()
    attach = driver.find_element(By.CSS_SELECTOR,"input[type='file']")
    attach.send_keys(midia)
    time.sleep(3)
    send = driver.find_element(By.CSS_SELECTOR,"span[data-icon='send']")
    send.click()

for contato in contatos:
    cade_contato(contato)
    enviar_mensagem(mensagem)
    enviar_midia(midia) 
    time.sleep(1)
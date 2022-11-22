import pywhatkit
import keyboard
import time
from datetime import datetime

contatos = ['+5511942419921', '+5511984207071']

while len(contatos) >= 1:
    pywhatkit.sendwhatmsg(contatos[0], 'Ignore esta mensagem', datetime.now().hour, datetime.now().minute + 1)
    del contatos [0]
    time.sleep(60)
    keyboard.press_and_release('ctrl + w')
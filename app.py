from selenium import webdriver
from selenium.webdriver.common.by import By
import webbrowser, pyautogui
from time import sleep


driver = webdriver.Chrome()
driver.get('https://www.tiktok.com/foryou?lang=pt-BR')
sleep(10)
#clicar no x do boot 
pyautogui.click(1020,118, duration= 2)
sleep(2)
#clicar em expandir a tela 
pyautogui.click(975,32, duration= 2)
sleep(2)
#clicar em entrar
pyautogui.click(1212,123,duration = 2)
sleep(5)
#Clicar em email
pyautogui.click(674,303, duration =2)
sleep(3)

#Clicar em insira o nome do usuario ou email
pyautogui.click(776,228, duration =2)
sleep(5)

#Prencher o login e senha 
#email
pyautogui.click(596,284, duration =2)
pyautogui.write('leonardogbarbosa16')
sleep(2)

#senha
pyautogui.click(606,325, duration =2)
pyautogui.write('123Leo456.')
sleep(2)

#clicar em Login
pyautogui.click(620,415, duration =3)
sleep(15)

#Navegar até a pagina que eu quero curtir tudo 
webbrowser.open('https://www.tiktok.com/@letspagnolo')
sleep(10)

#clicar na poastagem mais recente 
pyautogui.click(342,556, duration =3)
sleep(10)

#verificar se a postagem ja foi curtida 
for video in range(15):
    imagem_nao_curtida = pyautogui.locateAllOnScreen('naocurtida.png')
    imagem_curtida  = pyautogui.locateAllOnScreen('curtida.png')
    sleep(10)

    if imagem_curtida:
        #pule para proximo video 
        pyautogui.press('down')
        sleep(4)
    elif imagem_nao_curtida:
        #codigo para curtirda postagem
        imagem_nao_curtida = pyautogui.locateAllOnScreen('naocurtida.png')
        pyautogui.click('naocurtida.png') 
        sleep(4)
        pyautogui.press('down')




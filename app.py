from selenium import webdriver
from selenium.webdriver.common.by import By
import webbrowser, pyautogui
from time import sleep


driver = webdriver.Chrome()
driver.get('https://www.tiktok.com/foryou?lang=pt-BR')
sleep(20)
#clicar no x do boot 
pyautogui.click(1020,118, duration= 2)
sleep(2)
#clicar em expandir a tela 
pyautogui.click(975,32, duration= 2)
sleep(2)
#clicar em entrar
pyautogui.click(1247,147,duration = 2)
sleep(5)
#Clicar em email
pyautogui.click(654,326, duration =2)
sleep(2)

#Clicar em insira o nome do usuario ou email
pyautogui.click(720,258, duration =2)
sleep(2)

#Prencher o login e senha 
#email
pyautogui.click(596,284, duration =2)
pyautogui.write('leonardogbarbosa16')
sleep(2)

#senha
pyautogui.click(587,344, duration =2)
pyautogui.write('123Leo456.')
sleep(2)

#clicar em Login
pyautogui.click(644,420, duration =3)
sleep(30)

#Navegar até a pagina que eu quero curtir tudo 
webbrowser.open('https://www.tiktok.com/@letspagnolo')
sleep(10)

#clicar na poastagem mais recente 
pyautogui.click(342,556, duration =3)
sleep(5)

#verificar se a postagem ja foi curtida 
for video in range(15):
    imagem = pyautogui.locateAllOnScreen('curtida.png')
    sleep(2)

    if imagem:
        #pule para proximo video 
        pyautogui.press('down')
        sleep(4)
    else:
        #codigo para curtir a postagem
        sleep(4)
        driver.find_element(By.XPATH,"//<use [xlink:href='#heart-fill-52d919d9']")
        sleep(4)
        pyautogui.press('down')








import webbrowser, pyautogui
from time import sleep

webbrowser.open('https://www.tiktok.com/foryou?lang=pt-BR')
sleep(10)
#clicar em login
pyautogui.click(1231,144,duration = 2)
#Clicar em email
pyautogui.click(1013,330, duration =2)
#Clicar em insira o nome do usuario ou email
pyautogui.click(1095,256, duration =2)
#Prencher o login e senha 
#email
pyautogui.click(963,297, duration =2)
#senha
pyautogui.click(959,340, duration =2)
#clicar em entrar
pyautogui.click(975,428, duration =2)






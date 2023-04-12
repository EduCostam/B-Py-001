import pyautogui
import time

# Espera 5 segundos para abrir a plataforma
time.sleep(5)

# Loop infinito
while True:
    # Verifica se o número "123" aparece na plataforma
    if pyautogui.locateOnScreen('123.png') is not None:
        # Clica em um ponto especifico da tela
        pyautogui.click(x=100, y=200)
        # Espera 2 segundos
        time.sleep(2)
    # Verifica se o número "456" aparece na plataforma
    elif pyautogui.locateOnScreen('456.png') is not None:
        # Clica em outro ponto espefico da tela
        pyautogui.click(x=300, y=400)
        # Espera 2 segundos
        time.sleep(2)
    # Caso contrário, aguarda 1 segundo antes de verificar novamente
    else:
        time.sleep(1)

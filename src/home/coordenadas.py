import pyautogui
import time

# Encontra as posições das linhas amarela e azul na tela
yellow_line_pos = pyautogui.locateOnScreen('yellow_line.png')
blue_line_pos = pyautogui.locateOnScreen('blue_line.png')

# Encontra as posições dos botões na tela
inverter_button_pos = pyautogui.locateOnScreen('inverter_button.png')
vender_button_pos = pyautogui.locateOnScreen('vender_button.png')
comprar_button_pos = pyautogui.locateOnScreen('comprar_button.png')

# Loop principal do programa
while True:
    # Encontra a posição da barra verde na tela
    green_bar_pos = pyautogui.locateOnScreen('green_bar.png')

    # Verifica se a barra cruzou a linha amarela
    if green_bar_pos and green_bar_pos.top < yellow_line_pos.top:
        # Clica no botão "Inverter"
        pyautogui.click(inverter_button_pos)

    # Verifica se a barra cruzou a linha azul para baixo
    if green_bar_pos and green_bar_pos.top > blue_line_pos.top:
        # Clica no botão "Vender"
        pyautogui.click(vender_button_pos)

    # Verifica se a barra cruzou a linha azul para cima
    if green_bar_pos and green_bar_pos.top < blue_line_pos.top:
        # Clica no botão "Comprar"
        pyautogui.click(comprar_button_pos)

    # Verifica se a barra verde cruza a linha amarela
    if green_bar_pos and green_bar_pos.top < yellow_line_pos.top and \
            'last_green_bar_pos.top >= yellow_line_pos.top':
        pyautogui.click(inverter_button_pos)

    # Verifica se a barra verde cruza a linha azul para cima
    if green_bar_pos and green_bar_pos.top < blue_line_pos.top and \
            'last_green_bar_pos.top >= blue_line_pos.top':
        pyautogui.click(comprar_button_pos)

    # Verifica se a barra verde cruza a linha azul para baixo
    if green_bar_pos and green_bar_pos.top > blue_line_pos.top and \
            'last_green_bar_pos.top <= blue_line_pos.top':
        pyautogui.click(vender_button_pos)

    # Atualiza a posição da barra verde
    last_green_bar_pos = green_bar_pos

    # Aguarda um tempo para realizar a próxima verificação
    time.sleep(1)

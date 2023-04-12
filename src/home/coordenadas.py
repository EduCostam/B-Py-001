# Este código define as coordenadas dos pontos que o bot deve clicar e a
# plataforma emque ele deve
# verificar os números. As funções clicar_em_pontos e verificar_numeros são
# responsáveis por executar as ações especificadas. Em seguida, as funções são
# iniciadas em
# paralelo usando threads e o programa aguarda o término das threads antes de
# encerrar.


import threading
import pyautogui
import time

# definir as coordenadas dos pontos que o bot vai clicar
coordenadas = [(100, 100), (200, 200), (300, 300)]

# definir a plataforma em que o bot vai verificar os números
plataforma = "ExemploPlataforma"

# função para clicar em pontos especificos da tela


def clicar_em_pontos():
    for coord in coordenadas:
        pyautogui.click(coord)
        time.sleep(1)

# função para verificar números na plataforma especificada


def verificar_numeros():
    while True:
        numero = plataforma.verificar_numero()
        if numero == 10:
            pyautogui.click(500, 500)
        elif numero == 20:
            pyautogui.click(600, 600)
        elif numero == 30:
            pyautogui.click(700, 700)
        time.sleep(1)


# iniciar as funções em paralelo
pyautogui.PAUSE = 1  # definir um tempo de espera de 1 segundo entre cada
clicar_thread = threading.Thread(target=clicar_em_pontos)
verificar_thread = threading.Thread(target=verificar_numeros)

clicar_thread.start()
verificar_thread.join()

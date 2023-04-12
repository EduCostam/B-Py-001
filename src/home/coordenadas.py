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

# espera 2 segundos antes de começar a clicar
pyautogui.sleep(2)

# clica no botão na coordenada (100, 200)
pyautogui.click(100, 200)

# definir as coordenadas dos pontos que o bot vai clicar
coordenadas = [(100, 100), (200, 200), (300, 300)]

# definir a plataforma em que o bot vai verificar os números
plataforma = "ExemploPlataforma"


# função para encontrar a posição na tela do número 42 em uma plataforma
# específica

def find_number_42():
    platform_pos = pyautogui.locateOnScreen('platform_image.png')
    if platform_pos:
        number_pos = pyautogui.locateOnScreen(
            'number_42_image.png', region=platform_pos)
        if number_pos:
            return number_pos.center
    return None

# função para clicar em um ponto específico da tela


def click_screen_position(pos):
    if pos:
        pyautogui.click(pos)


# loop principal do bot
while True:
    # verificar se o número 42 apareceu na plataforma
    number_pos = find_number_42()
    if number_pos:
        # clicar no número 42
        click_screen_position(number_pos)
        # esperar 1 segundo para a próxima ação
        time.sleep(1)
        # clicar em outro ponto específico da tela
        click_screen_position((100, 100))
        # esperar 3 segundos para a próxima verificação
        time.sleep(3)


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


def monitorar_plataforma():
    while True:
        # Captura uma imagem da tela e salva em um arquivo temporário
        imagem_temporaria = pyautogui.screenshot(region=(0, 0, 1920, 1080))

        # Busca por uma imagem que contém o número "123" na tela
        if pyautogui.locateOnScreen('123.png', image=imagem_temporaria,
                                    grayscale=True, confidence=0.8):
            # Se encontrar o número, clica em um ponto específico na tela
            pyautogui.click(x=100, y=100)

        # Espera um segundo antes de realizar a próxima busca
        time.sleep(1)

        def main():
            "login"()
            "realizar_tarefa_1"()
            "realizar_tarefa_2"()
            "monitorar_plataforma"()

        if __name__ == '__main__':
            main()


# Definindo as coordenadas dos pontos que o bot deve clicar
ponto1 = (100, 200)
ponto2 = (300, 400)
ponto3 = (500, 600)

# Definindo a plataforma e o número que o bot deve buscar
plataforma = "Plataforma X"
numero = 1234

# Loop principal do bot
while True:
    # Busca pela plataforma
    pyautogui.press('win')
    pyautogui.write(plataforma)
    pyautogui.press('enter')
    time.sleep(5)  # Aguarda a plataforma abrir

    # Verifica se o número está presente na plataforma
    if pyautogui.locateOnScreen('numero.png', confidence=0.9) is not None:
        # Se o número estiver presente, clica nos pontos específicos da tela
        pyautogui.click(ponto1)
        time.sleep(2)
        pyautogui.click(ponto2)
        time.sleep(2)
        pyautogui.click(ponto3)
        time.sleep(2)

    # Aguarda um tempo antes de buscar novamente
    time.sleep(10)


# iniciar as funções em paralelo
pyautogui.PAUSE = 1  # definir um tempo de espera de 1 segundo entre cada
clicar_thread = threading.Thread(target=clicar_em_pontos)
verificar_thread = threading.Thread(target=verificar_numeros)

clicar_thread.start()
verificar_thread.join()

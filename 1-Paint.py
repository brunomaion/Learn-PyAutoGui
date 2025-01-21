import pyautogui

# Obter tamanho da tela
screenWidth, screenHeight = pyautogui.size()
currentMouseX, currentMouseY = pyautogui.position()

print(screenWidth, screenHeight)

# Mover o cursor para o botão iniciar e clicar
start_button_x = screenWidth/2 - 190  # Coordenada X do botão iniciar
start_button_y = screenHeight - 20  # Coordenada Y do botão iniciar

pyautogui.moveTo(start_button_x, start_button_y)
pyautogui.click()

pyautogui.sleep(1)
# Digitar "paint" e pressionar Enter
pyautogui.write('paint')
pyautogui.sleep(1)
pyautogui.press('enter')
# Pressionar a tecla F11 para entrar em tela cheia
pyautogui.sleep(1)


# Esperar a imagem abrir
pyautogui.sleep(2)

# Encontrar a imagem na tela e clicar nela
image_location = pyautogui.locateOnScreen('imagens/1-lataDeTinta.png', confidence=.70)
image_center = pyautogui.center(image_location)
pyautogui.moveTo(image_center)
pyautogui.click()

# Esperar a imagem abrir

# Encontrar a imagem na tela e clicar nela


image_location = pyautogui.locateOnScreen('imagens/2-corVerde.png', confidence=.70)
image_center = pyautogui.center(image_location)
pyautogui.moveTo(image_center)
pyautogui.click()



# Mover o cursor para o centro da tela e clicar
center_x = screenWidth / 2
center_y = screenHeight / 2

pyautogui.moveTo(center_x, center_y)
pyautogui.sleep(1)


pyautogui.click()
pyautogui.click()
pyautogui.click()
pyautogui.sleep(1)
# Pressionar as teclas Ctrl+Shift+S para salvar
pyautogui.hotkey('ctrl', 's')
pyautogui.sleep(1)
pyautogui.write('teste')
pyautogui.hotkey('enter')


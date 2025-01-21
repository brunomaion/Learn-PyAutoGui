import pyautogui

pyautogui.hotkey('win', 'r')
pyautogui.hotkey('enter')
pyautogui.sleep(1)
pyautogui.write('python --version')
pyautogui.hotkey('enter')

pyautogui.hotkey('win', 'up')
pyautogui.sleep(1)
# Tira um print e salva como "screenshot.png"
pyautogui.screenshot("imagens/3-pyVersion.png")
print("Captura de tela salva como 'screenshot.png'")
pyautogui.hotkey('alt', 'f4')
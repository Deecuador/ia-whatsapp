import pyautogui
import time

# Pausa global para evitar ejecución demasiado rápida
pyautogui.PAUSE = 0.5  # Intervalo global entre cada acción

# Espera inicial de 2 segundos para darte tiempo de posicionar la ventana adecuada
time.sleep(2)

# Acción 1: Mover y hacer clic en una posición específica
pyautogui.moveTo(178, 367, duration=1)  # Mueve a posición (290, 318)
pyautogui.click()

# Acción 2: Mover a otra posición y hacer clic
pyautogui.moveTo(822, 702, duration=1)
pyautogui.click()

# Pausa breve antes de escribir el texto
time.sleep(1)

# Acción 3: Escribir el texto
texto = "Jajaja pendiente causa ya estamos por aca..!!!!!"
pyautogui.write(texto, interval=0.1)  # Escribe el texto con un retraso de 0.1 segundos por tecla

# Acción 4: Mover y hacer clic en una tercera posición
pyautogui.moveTo(1330, 702, duration=1)
pyautogui.click()

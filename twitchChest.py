import pyautogui
import time
import keyboard
import winsound

#from pynput.keyboard import Listener


# LEEMOS TECLA P -> GUARDAMOS PUNTO DEL RATON
# LEEMOS TECLA P -> GUARDAMOS SEGUNDO PUNTO DEL RATON

# CADA X TIEMPO MIRAMOS EL COLOR

print("CLICA CUALQUIER KEY BRO")

keyboard.read_key()
print(pyautogui.position())
(pos1X, pos1Y) = pyautogui.position()
winsound.PlaySound("SystemExclamation", winsound.SND_ALIAS)

print("GOT IT")

print("EJECUTADO EN 5 SEGUNDOS...")
time.sleep(5)
print("EJECUTADO")

while True:
    if pyautogui.pixelMatchesColor(pos1X, pos1Y, (0,245,147)) or pyautogui.pixelMatchesColor(pos1X, pos1Y, (0,173,150)):
        (recoverX, recoverY) = pyautogui.position()
        pyautogui.click(pos1X, pos1Y)
        pyautogui.moveTo(recoverX, recoverY)
        winsound.MessageBeep()
        print("COFRE")

    time.sleep(5)

# SI EL COLOR CORRESPONDE, CLICA (0,245,147) o (0,173,150)
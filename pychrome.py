import pyautogui
import time
#time.sleep(4)
#pos=pyautogui.position()
#print(pos);
#time.sleep(4)
#exit()
time.sleep(10)
pyautogui.press('win')
time.sleep(10)
pyautogui.write('chrome')
time.sleep(10)
#pyautogui.press('down')
#pyautogui.Pause = 5
pyautogui.press('enter')
time.sleep(4)
#chome aberto
pyautogui.click(x=799, y=582)
time.sleep(4)
pyautogui.click(x=1768, y=52)
time.sleep(4)
x=0
for i in range(20):
    if x==0:
        x=1
    #clica na extenção
    if x > 1:
        pyautogui.click(x=1768, y=52)
    time.sleep(4)
    pyautogui.click(x=1566, y=211)
    time.sleep(4)
    pyautogui.click(x=1671, y=263)
    time.sleep(4)
    pyautogui.click(x=1673, y=410)
    time.sleep(70)
    x=x+1

exit()
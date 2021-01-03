import pyautogui as pag
import time
# while 1:
#     x,y = pag.position()
#     print(x,y)

x,y = 487, 327
cnt = 1

def transfer():
    pag.hotkey('ctrl', 'v')
    pag.press('enter')
    time.sleep(2)
    pag.press('esc')

# 1. 위치 이동
pag.moveTo(x,y)
time.sleep(0.5)
pag.doubleClick()
transfer()

while 1:
    # 3. 위치 이동 후 다시 반복
    pag.press('down')
    time.sleep(0.2)
    pag.press('enter')
    transfer()
    cnt += 1

    if cnt == 1228:
        break


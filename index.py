import pyautogui as pag
import time

# while 1:
#     x,y = pag.position()
#     print(x,y)

# while문을 통한 x,y좌표 기억하여 변수에 대입하기.
x,y = 487, 327
start = 1
end = 100 # 현재 커서를 기준으로 보내고 싶은 인원의 수

def transfer():
    # 대화방 접속
    pag.press('enter')
    # 파일 전송
    pag.hotkey('ctrl', 'v')
    pag.press('enter')
    time.sleep(0.5) # 0.5초의 딜레이
    # 대화방 나오기
    pag.press('esc')
    # 아래 친구로 이동
    pag.press('down')

# 1. 마우스 위치 이동
pag.moveTo(x,y)
# 2. 대화방 클릭
pag.click()
# 3. 대화방 접속 후 파일전송하기
transfer()

# 4. while문을 통한 매크로 진행
while 1:
   	# 만약 end의 인원만큼 보냈다면 프로그램 종료
    if start == end:
        break

    # 4.1 매크로 진행
    transfer()
    #4.2 매크로 진행마다 보낸 사람의 수 중가
    start += 1

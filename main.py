import pyautogui as py
import time

py.click(300, 850, duration = 1)
py.hotkey('command', 't')
py.click(600,80, duration= 1)
py.write('https://github.com/')
py.hotkey('enter')
py.click(1230,140, duration = 2)
py.click(650,320,duration =1)
py.write('alexandru13.1997@gmail.com')
py.click(650,400,duration =1)
py.write('438be6A$')
py.click(800,450,duration =1) #sign in
py.click(1400,130,duration =3)
py.click(1370,280, duration =1)
py.click(490,340,duration =2)
py.click(460,400,duration =2)
py.click(735, 515, duration =2)
py.click(735,220, duration =2)
py.hotkey('shift','command','h')
py.click(930,425, duration = 1)
py.click(930,360, duration = 1)
py.click(930,315, duration = 1)
py.click(1060,615, duration = 1)
time.sleep(2)
py.scroll(-5)
py.click(245,739, duration = 2)

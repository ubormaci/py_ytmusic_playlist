# tehat
# amikor elindul, akkor raklikkel egy adott poziciora
# es kimasolja onnan a szoveget
# bepasteli egy fajlba
# klikkel egy masik poziciora
# var egy kicsit
# repeat

# effektive a main monitoron van kinyitv a yt music (fullscreen)
# eloszor kimasolja a mostani video linkjet
# aztan megy a kovetkezore

import pyautogui as pg
import time
import pyperclip as pc
import random

posup = (1375, 58)
posnext = (138, 1004)

prev:str = "dummy starting text"
text:str = "current text"

while(prev != text):
    pg.click(x=posup[0], y=posup[1])
    time.sleep(0.5)
    pg.hotkey('ctrl', 'a')
    time.sleep(0.5)
    pg.hotkey('ctrl', 'c')

    prev = text
    text = pc.paste()
    if(prev == text):
        break
    with open("out.txt", "a") as f:
        f.write(text)
        f.write("\n")
    pg.click(x=posnext[0], y=posnext[1])
    time.sleep(random.random())
    
print("Successfully finished reading list")

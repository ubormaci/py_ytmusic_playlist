# tehat megvannak a linkek
# most csak kell importaljuk mediahuman-ba
# es a lenyeg az, hogy olyan sorrendben akarjuk hogy letoltodjenek
# ahogy youtube-on vannak

import pyautogui as pg
import time
import pyperclip as pc
import random

inp:str = "out.txt"

with open(inp, "r") as f:
    raw = f.read()
    
links = raw.splitlines() 
    
ctr:int = 1
tot:int = len(links)
    
for link in links:
    print(f"{ctr}/{tot}:{link}")
    ctr += 1
    pc.copy(link)
    eep = 0.5
    time.sleep(eep)
    
        
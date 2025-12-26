# tehat megvannak a linkek
# most csak kell importaljuk mediahuman-ba
# es a lenyeg az, hogy olyan sorrendben akarjuk hogy letoltodjenek
# ahogy youtube-on vannak

import pyautogui as pg
import time
import pyperclip as pc
import random
import yt_dlp
from datetime import datetime

inp:str = "inp.txt"

with open(inp, "r") as f:
    raw = f.read()
    
links = raw.splitlines() 
    
ctr:int = 1
tot:int = len(links)

def sanity_check(info):
    formats = info.get("formats", [])
    audio_formats = [
        f for f in formats
        if f.get("vcodec") == "none" and f.get("acodec") != "none"
    ]

    if len(audio_formats) < 3:
        raise RuntimeError(
            f"Suspicious format list ({len(audio_formats)} audio formats). "
            "Possible rate limiting or JS failure."
        )

ydl_opts = {
    "format": "bestaudio/best",
    "outtmpl": "date/%(title)s-%(epoch)s.%(ext)s",
    "postprocessors": [
        {
            "key": "FFmpegExtractAudio",
            "preferredcodec": "mp3",
            "preferredquality": "192",
        },
        {
            "key": "FFmpegMetadata",
        },
        {   
            "key": "EmbedThumbnail"
        },
    ],
    "noplaylist": True,
    
    "js_runtimes": {
        "node": {}
    },
    
    "remote_components": ["ejs:github"],

    "post_extract_hooks": [sanity_check],
    
    "addmetadata": True,
    "writethumbnail": True,
    "convert_thumbnails": "png",

    "sleep_interval": 10,
    "max_sleep_interval": 30,
    "extractor_retries": 5,
    "fragment_retries": 5,
    "retry_sleep_functions": {"http": lambda n: 5 * n},
}

ydl = yt_dlp.YoutubeDL(ydl_opts)

for link in links:
    
    print(f"\n\n{ctr}/{tot}:{link}\n\n")
    ctr += 1
    #pc.copy(link)
    
    #pc.copy(link)   # unchanged
    #time.sleep(0.5)

    try:
        ydl.download([link])
    except Exception as e:
        print(f"FAILED: {link}")
        raise()
        
    eep = random.uniform(10, 20)
    time.sleep(eep)
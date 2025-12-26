from pathlib import Path
from math import log10, ceil

folder = Path("date")
files = sorted(folder.glob('*'), key=lambda f: f.stat().st_mtime)

tot:int = len(files)
namelen:int = ceil(log10(tot+1))

ctr:int = 1

for file in sorted(folder.glob('*'), key=lambda f: f.stat().st_mtime):
    print(f"{file.name}", end=" ")
    
    next_str = f"{ctr:0{namelen}d}"
        
    ctr += 1        

    # build new filename
    newname = folder / f"{next_str} - {file.name}"
    
    
    file.rename(newname)
    print(f"-> {newname}")
    
    

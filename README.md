So there I was one day, wanting to download the songs I've been listening to lately- I had a nice little Youtube Music playlist and everything. Only to find out, that the program that I've been using until then, Mediahuman, when prompted with a Youtube Music playlist link, opens it in Youtube instead. And surprises of surprises, some songs just *aren't* present in the Youtube version of the playlist.

So this is my solution to that, a series of three scripts: the first one automates copying all the links one by one, the second one downloads them, the third one renames them so the files retain their order from the playlist.

To be more precise:
* fullscreen.py moves to mouse first to the title bar, copies the link, then moves it to the position of the "next" button. It does this until it sees a link repeating, at which point it stops.
* down.py and mh.py both serve to download them. "mh" refers to Mediahuman, which had the settings to automatically start downloading songs when their link was copied onto the clipboard. Download is the newer/more polished script, which uses ytdlp.
* rename.py renames the songs sequentially, with padded zeroes, based on their time created, ascending.

To do:
* Fix the issue where it occasionally gets confused about special (ex. Hungarian) characters
* Get cover arts in 4:3 where available

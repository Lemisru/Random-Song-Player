from random import choice
import os
import eel

def resolve_path(path):
    if getattr(os.sys, "frozen", False):
        resolved_path = os.path.abspath(os.path.join(os.sys._MEIPASS, path))
    else:
        resolved_path = os.path.abspath(os.path.join(os.getcwd(), path))

    return resolved_path

path = "C:/Users/Lemis/AppData/Local/GeometryDash/"

songs = []
for file in os.listdir(path):
    if ".ogg" in file or ".dat" in file:
        continue
    songs.append("/"+file)

@eel.expose
def start_song():
    os.startfile(resolve_path(path)+choice(songs))

eel.init("web")
eel.start("main.html", size=(300,450), mode="default")
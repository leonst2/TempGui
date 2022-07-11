import customtkinter as ctk
import threading
import Colorpalet as cp
import Data as data
from MainFrame import GraphFrame

window = ctk.CTk()


#screen size settings
def setFullscreen(event):
    window.attributes('-fullscreen', True)


def noFullscreen(event):
    window.attributes('-fullscreen', False)


screen_w = window.winfo_screenwidth()
screen_h = window.winfo_screenheight()
app_h = 1080
app_w = 1920
posX = (screen_w / 2) - (app_w / 2)
posY = (screen_h / 2) - (app_h / 2)

#window.geometry(f'{app_w}x{app_h}+{int(posX)}+{int(posY)}')
window.attributes("-fullscreen", False)
window.title("Temperature-Master")
window.resizable(True, True)
window.iconbitmap(default="logo02.ico")
window.grid_columnconfigure(1, weight=1)
window.grid_rowconfigure(0, weight=1)
window.bind("<F11>", setFullscreen)
window.bind("<Escape>", noFullscreen)

mainView = GraphFrame(master=window)

if __name__ == '__main__':
    window.mainloop()

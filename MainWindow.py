import os
from tkinter.ttk import Progressbar
import customtkinter as ctk
import win32con
import win32gui
from PIL import Image, ImageTk
# import Data as data
from MainFrame import GraphFrame

#hide = win32gui.GetForegroundWindow()
#win32gui.ShowWindow(hide, win32con.SW_HIDE)


def mainApp():

    # screen size settings
    def setFullscreen(event):
        window.attributes('-fullscreen', True)

    def noFullscreen(event):
        window.attributes('-fullscreen', False)

    window = ctk.CTk()
    window.state("zoomed")
    window.title("Temperature-Master")
    window.resizable(True, True)
    window.iconbitmap(default=PATH+"/images/icon.ico")
    window.grid_columnconfigure(1, weight=1)
    window.grid_rowconfigure(0, weight=1)
    window.bind("<F11>", setFullscreen)
    window.bind("<Escape>", noFullscreen)

    mainView = GraphFrame(master=window)

    if __name__ == '__main__':
        window.mainloop()


prog = 0
splash = ctk.CTk()

PATH = os.path.dirname(os.path.realpath(__file__))

screen_w = splash.winfo_screenwidth()
screen_h = splash.winfo_screenheight()
app_h = 500
app_w = 700
posX = (screen_w / 2) - (app_w / 2)
posY = (screen_h / 2) - (app_h / 2)

splash.title("Splash")
splash.geometry(f'{app_w}x{app_h}+{int(posX)}+{int(posY)}')
splash.overrideredirect(True)

container = ctk.CTkFrame(bg_color="white", fg_color="white")
container.pack(side=ctk.TOP, fill="both", pady=10, padx=10, expand=True)

logo = ImageTk.PhotoImage(Image.open(PATH + "/images/logo.jfif").resize((700, 350)))
image_frame = ctk.CTkLabel(master=container, image=logo)
image_frame.pack()

computer = ImageTk.PhotoImage(Image.open(PATH + "/images/computer.jpg").resize((80, 80)))
computer_container = ctk.CTkLabel(master=container, image=computer, height=80, width=80)
computer_container.pack(side=ctk.LEFT, padx=10, pady=20)

database = ImageTk.PhotoImage(Image.open(PATH + "/images/database.png").resize((80, 80)))
database_container = ctk.CTkLabel(master=container, image=database, height=80, width=80)
database_container.pack(side=ctk.RIGHT, padx=10, pady=20)

check_container = ctk.CTkLabel(master=container, height=40, fg_color="white", text="")
check_container.pack(side=ctk.BOTTOM, padx=40, pady=10)

bar = Progressbar(container, mode="determinate")
bar.pack(side=ctk.BOTTOM, fill="x", padx=0, pady=10)


def progress():
    global prog
    if prog != 100:
        bar['value'] += 2
        prog += 2
        splash.after(25, progress)
    else:
        splash.after(1000, kill_splash)


def kill_splash():
    check_container.configure(text="Successfully connected!", fg_color="lightgreen")
    splash.update_idletasks()
    splash.after(1000)
    splash.destroy()
    mainApp()


splash.after(1000, progress)
splash.mainloop()


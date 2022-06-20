import customtkinter as ctk
import Colorpalet as cp
import GraphFrame as gp
from PIL import Image, ImageTk
import os


class SideFrame(ctk.CTkFrame):

    def __init__(self, master, width, fgcolor):
        super().__init__(master, width=width)

        PATH = os.path.dirname(os.path.realpath(__file__))
        skale_img = ImageTk.PhotoImage(Image.open(PATH + "/images/skale.png").resize((20, 20), Image.ANTIALIAS))
        temp_img = ImageTk.PhotoImage(Image.open(PATH + "/images/temperature.png").resize((20, 20), Image.ANTIALIAS))
        pres_img = ImageTk.PhotoImage(Image.open(PATH + "/images/pressure.png").resize((20, 20), Image.ANTIALIAS))
        hum_img = ImageTk.PhotoImage(Image.open(PATH + "/images/humidity.png").resize((20, 20), Image.ANTIALIAS))
        list_img = ImageTk.PhotoImage(Image.open(PATH + "/images/list.png").resize((20, 20), Image.ANTIALIAS))
        news_img = ImageTk.PhotoImage(Image.open(PATH + "/images/news.png").resize((20, 20), Image.ANTIALIAS))
        set_img = ImageTk.PhotoImage(Image.open(PATH + "/images/settings.png").resize((20, 20), Image.ANTIALIAS))
        pro_img = ImageTk.PhotoImage(Image.open(PATH + "/images/profile.png").resize((20, 20), Image.ANTIALIAS))

        def set_value_select(value):
            gp.GraphFrame.value_select = value

        def hover_info(event, btn, select):
            if select:
                info_entry.configure(text=btn.text)
                if str(btn) == ".!ctkframe.!ctkbutton":
                    info_entry.configure(text="All data")
                if str(btn) == ".!ctkframe.!ctkbutton2":
                    info_entry.configure(text="Temperature")
                if str(btn) == ".!ctkframe.!ctkbutton3":
                    info_entry.configure(text="Pressure")
                if str(btn) == ".!ctkframe.!ctkbutton4":
                    info_entry.configure(text="Humidity")
                if str(btn) == ".!ctkframe.!ctkbutton5":
                    info_entry.configure(text="List View")
                if str(btn) == ".!ctkframe.!ctkbutton6":
                    info_entry.configure(text="Profile")
                if str(btn) == ".!ctkframe.!ctkbutton7":
                    info_entry.configure(text="Settings")
                if str(btn) == ".!ctkframe.!ctkbutton8":
                    info_entry.configure(text="News")
            else:
                info_entry.configure(text="")

        sideFrame = ctk.CTkFrame(master=master, width=width, fg_color=fgcolor, corner_radius=0)
        sideFrame.grid(row=0, column=0, sticky="nswe")

        info_entry = ctk.CTkLabel(master=sideFrame, fg_color="white", text="")
        info_entry.pack(side=ctk.TOP, fill='x', padx=10, pady=20)

        btn_graph = ctk.CTkButton(master=sideFrame, image=skale_img, text="", width=80, height=60, compound="right", fg_color=cp.blue, cursor="arrow", command=set_value_select(0))
        btn_graph.pack(side=ctk.TOP, fill='x', padx=10, pady=0)
        btn_graph.bind("<Enter>", lambda event, btn=btn_graph, select=True: hover_info(event, btn, select))
        btn_graph.bind("<Leave>", lambda event, btn=btn_graph, select=False: hover_info(event, btn, select))

        btn_temp = ctk.CTkButton(master=sideFrame, image=temp_img, text="", width=80, height=60, compound="right", fg_color=cp.blue, cursor="arrow", command=set_value_select(1))
        btn_temp.pack(side=ctk.TOP, fill='x', padx=10, pady=20)
        btn_temp.bind("<Enter>", lambda event, btn=btn_temp, select=True: hover_info(event, btn, select))
        btn_temp.bind("<Leave>", lambda event, btn=btn_temp, select=False: hover_info(event, btn, select))

        btn_pressure = ctk.CTkButton(master=sideFrame, image=pres_img, text="", width=80, height=60, compound="right", fg_color=cp.blue, cursor="arrow", command=set_value_select(2))
        btn_pressure.pack(side=ctk.TOP, fill='x', padx=10, pady=0)
        btn_pressure.bind("<Enter>", lambda event, btn=btn_pressure, select=True: hover_info(event, btn, select))
        btn_pressure.bind("<Leave>", lambda event, btn=btn_pressure, select=False: hover_info(event, btn, select))

        btn_humidity = ctk.CTkButton(master=sideFrame, image=hum_img, text="", width=80, height=60, compound="right", fg_color=cp.blue, cursor="arrow", command=set_value_select(3))
        btn_humidity.pack(side=ctk.TOP, fill='x', padx=10, pady=20)
        btn_humidity.bind("<Enter>", lambda event, btn=btn_humidity, select=True: hover_info(event, btn, select))
        btn_humidity.bind("<Leave>", lambda event, btn=btn_humidity, select=False: hover_info(event, btn, select))

        btn_list = ctk.CTkButton(master=sideFrame, image=list_img, text="", width=80, height=60, compound="right", fg_color=cp.blue, cursor="arrow", command=set_value_select(4))
        btn_list.pack(side=ctk.TOP, fill='x', padx=10, pady=0)
        btn_list.bind("<Enter>", lambda event, btn=btn_list, select=True: hover_info(event, btn, select))
        btn_list.bind("<Leave>", lambda event, btn=btn_list, select=False: hover_info(event, btn, select))

        btn_profile = ctk.CTkButton(master=sideFrame, image=pro_img, text="", width=80, height=60, compound="right", fg_color=cp.blue, cursor="arrow")
        btn_profile.pack(side=ctk.BOTTOM, fill='x', padx=10, pady=20)
        btn_profile.bind("<Enter>", lambda event, btn=btn_profile, select=True: hover_info(event, btn, select))
        btn_profile.bind("<Leave>", lambda event, btn=btn_profile, select=False: hover_info(event, btn, select))

        btn_settings = ctk.CTkButton(master=sideFrame, image=set_img, text="", width=80, height=60, compound="right", fg_color=cp.blue, cursor="arrow")
        btn_settings.pack(side=ctk.BOTTOM, fill='x', padx=10, pady=0)
        btn_settings.bind("<Enter>", lambda event, btn=btn_settings, select=True: hover_info(event, btn, select))
        btn_settings.bind("<Leave>", lambda event, btn=btn_settings, select=False: hover_info(event, btn, select))

        btn_news = ctk.CTkButton(master=sideFrame, image=news_img, text="", width=80, height=60, compound="right", fg_color=cp.blue, cursor="arrow")
        btn_news.pack(side=ctk.BOTTOM, fill='x', padx=10, pady=20)
        btn_news.bind("<Enter>", lambda event, btn=btn_news, select=True: hover_info(event, btn, select))
        btn_news.bind("<Leave>", lambda event, btn=btn_news, select=False: hover_info(event, btn, select))

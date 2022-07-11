import customtkinter as ctk
import Colorpalet as cp
import threading
import Data as data
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
from PIL import Image, ImageTk
import os


class GraphFrame(ctk.CTkFrame):
    live_state = False
    toggle_state = 0
    category = 0

    def __init__(self, master):
        super().__init__(master)

        # ----------Methods----------
        def select_button(btn_active):
            btn1.configure(fg_color=cp.lightGrey)
            btn1.configure(cursor="hand2", state="normal")
            btn2.configure(fg_color=cp.lightGrey)
            btn2.configure(cursor="hand2", state="normal")
            btn3.configure(fg_color=cp.lightGrey)
            btn3.configure(cursor="hand2", state="normal")
            btn4.configure(fg_color=cp.lightGrey)
            btn4.configure(cursor="hand2", state="normal")
            btn_active.configure(fg_color=cp.darkGrey, state="disabled", cursor="arrow")

        def load_graph(value_x, value_y):
            plot1.clear()
            plot1.plot(value_x, value_y)
            # plot1.set_ylim(ymin=0, ymax=30)
            canvas1.draw()
            canvas1.get_tk_widget().pack(side=ctk.TOP, fill='x', padx=40, pady=40)

        def live_graph():
            #btn1.configure(cursor="hand2", state="normal")
            #self.stop = 0
            plot1.clear()
            if self.category == 1:
                plot1.plot(data.live_time, data.live_temp)
            elif self.category == 2:
                plot1.plot(data.live_time, data.live_humidity)
            elif self.category == 3:
                plot1.plot(data.live_time, data.live_pressure)
            # plot1.set_ylim(ymin=0, ymax=30)
            canvas1.draw()
            canvas1.get_tk_widget().pack(side=ctk.TOP, fill='x', padx=40, pady=40)
            master.after(10000, lambda: [live_graph()])

        def plot_new(category):
            self.category = category
            data.set_current_data(category)
            if self.toggle_state == 1:
                self.live_state = False
                load_graph(data.today_time, data.current_today)
            elif self.toggle_state == 2:
                load_graph(data.hours_time, data.current_hours)
            elif self.toggle_state == 3:
                load_graph(data.week_time, data.current_week)
            elif self.toggle_state == 0:
                self.live_state = True
                live_graph()

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

        #----------Graph Frame----------
        graphFrame = ctk.CTkFrame(master=master, fg_color=cp.lightGrey, corner_radius=10)
        graphFrame.grid(row=0, column=1, sticky="nswe", pady=20, padx=20)

        tabBar = ctk.CTkFrame(graphFrame, fg_color=cp.darkGrey, border_color=cp.darkGrey)
        tabBar.pack(side=ctk.TOP, padx=40, pady=10)
        btn1 = ctk.CTkButton(tabBar, corner_radius=0, text="LIVE", width=100, hover_color=cp.darkGrey,
                             fg_color=cp.darkGrey, command=lambda: [select_button(btn1), ])
        btn1.pack(side=ctk.LEFT)
        btn2 = ctk.CTkButton(tabBar, corner_radius=0, text="TODAY", width=100, hover_color=cp.darkGrey,
                             fg_color=cp.lightGrey, command=lambda: [select_button(btn2)])
        btn2.pack(side=ctk.LEFT)
        btn3 = ctk.CTkButton(tabBar, corner_radius=0, text="24-HOURS", width=100, hover_color=cp.darkGrey,
                             fg_color=cp.lightGrey, command=lambda: [select_button(btn3)])
        btn3.pack(side=ctk.LEFT)
        btn4 = ctk.CTkButton(tabBar, corner_radius=0, text="1-WEEK", width=100, hover_color=cp.darkGrey,
                             fg_color=cp.lightGrey, command=lambda: [select_button(btn4)])
        btn4.pack(side=ctk.LEFT)

        fig = Figure(figsize=(16, 9))
        plot1 = fig.add_subplot(111)
        plot1.plot([], [])
        canvas1 = FigureCanvasTkAgg(fig, graphFrame)
        canvas1.draw()
        canvas1.get_tk_widget().pack(side=ctk.TOP, fill='x', padx=40, pady=40)

        # ----------Admin Frame----------
        adminFrame = ctk.CTkFrame(master=master, fg_color=cp.lightGrey, corner_radius=10)
        adminFrame.grid(row=0, column=1, sticky="nswe", pady=20, padx=20)
        graphFrame.tkraise()

        # Side Frame
        PATH = os.path.dirname(os.path.realpath(__file__))
        skale_img = ImageTk.PhotoImage(Image.open(PATH + "/images/skale.png").resize((20, 20), Image.ANTIALIAS))
        temp_img = ImageTk.PhotoImage(Image.open(PATH + "/images/temperature.png").resize((20, 20), Image.ANTIALIAS))
        pres_img = ImageTk.PhotoImage(Image.open(PATH + "/images/pressure.png").resize((20, 20), Image.ANTIALIAS))
        hum_img = ImageTk.PhotoImage(Image.open(PATH + "/images/humidity.png").resize((20, 20), Image.ANTIALIAS))
        list_img = ImageTk.PhotoImage(Image.open(PATH + "/images/list.png").resize((20, 20), Image.ANTIALIAS))
        news_img = ImageTk.PhotoImage(Image.open(PATH + "/images/news.png").resize((20, 20), Image.ANTIALIAS))
        set_img = ImageTk.PhotoImage(Image.open(PATH + "/images/settings.png").resize((20, 20), Image.ANTIALIAS))
        pro_img = ImageTk.PhotoImage(Image.open(PATH + "/images/profile.png").resize((20, 20), Image.ANTIALIAS))

        sideFrame = ctk.CTkFrame(master=master, width=100, fg_color=cp.lightGrey, corner_radius=0)
        sideFrame.grid(row=0, column=0, sticky="nswe")

        info_entry = ctk.CTkLabel(master=sideFrame, fg_color="white", text="")
        info_entry.pack(side=ctk.TOP, fill='x', padx=10, pady=20)

        btn_graph = ctk.CTkButton(master=sideFrame, image=skale_img, text="", width=80, height=60, compound="right",
                                  fg_color=cp.blue, cursor="hand2",
                                  command=lambda: [])
        btn_graph.pack(side=ctk.TOP, fill='x', padx=10, pady=0)
        btn_graph.bind("<Enter>", lambda event, btn=btn_graph, select=True: hover_info(event, btn, select))
        btn_graph.bind("<Leave>", lambda event, btn=btn_graph, select=False: hover_info(event, btn, select))

        btn_temp = ctk.CTkButton(master=sideFrame, image=temp_img, text="", width=80, height=60, compound="right",
                                 fg_color=cp.blue, cursor="hand2",
                                 command=lambda: [plot_new(1)])
        btn_temp.pack(side=ctk.TOP, fill='x', padx=10, pady=20)
        btn_temp.bind("<Enter>", lambda event, btn=btn_temp, select=True: hover_info(event, btn, select))
        btn_temp.bind("<Leave>", lambda event, btn=btn_temp, select=False: hover_info(event, btn, select))

        btn_pressure = ctk.CTkButton(master=sideFrame, image=pres_img, text="", width=80, height=60, compound="right",
                                     fg_color=cp.blue, cursor="hand2",
                                     command=lambda: [plot_new(2)])
        btn_pressure.pack(side=ctk.TOP, fill='x', padx=10, pady=0)
        btn_pressure.bind("<Enter>", lambda event, btn=btn_pressure, select=True: hover_info(event, btn, select))
        btn_pressure.bind("<Leave>", lambda event, btn=btn_pressure, select=False: hover_info(event, btn, select))

        btn_humidity = ctk.CTkButton(master=sideFrame, image=hum_img, text="", width=80, height=60, compound="right",
                                     fg_color=cp.blue, cursor="hand2",
                                     command=lambda: [plot_new(3)])
        btn_humidity.pack(side=ctk.TOP, fill='x', padx=10, pady=20)
        btn_humidity.bind("<Enter>", lambda event, btn=btn_humidity, select=True: hover_info(event, btn, select))
        btn_humidity.bind("<Leave>", lambda event, btn=btn_humidity, select=False: hover_info(event, btn, select))

        btn_list = ctk.CTkButton(master=sideFrame, image=list_img, text="", width=80, height=60, compound="right",
                                 fg_color=cp.blue, cursor="hand2",
                                 command=lambda: [])
        btn_list.pack(side=ctk.TOP, fill='x', padx=10, pady=0)
        btn_list.bind("<Enter>", lambda event, btn=btn_list, select=True: hover_info(event, btn, select))
        btn_list.bind("<Leave>", lambda event, btn=btn_list, select=False: hover_info(event, btn, select))

        btn_profile = ctk.CTkButton(master=sideFrame, image=pro_img, text="", width=80, height=60, compound="right",
                                    fg_color=cp.blue, cursor="hand2",
                                    command=lambda: [])
        btn_profile.pack(side=ctk.BOTTOM, fill='x', padx=10, pady=20)
        btn_profile.bind("<Enter>", lambda event, btn=btn_profile, select=True: hover_info(event, btn, select))
        btn_profile.bind("<Leave>", lambda event, btn=btn_profile, select=False: hover_info(event, btn, select))

        btn_settings = ctk.CTkButton(master=sideFrame, image=set_img, text="", width=80, height=60, compound="right",
                                     fg_color=cp.blue, cursor="hand2",
                                     command=lambda: [])
        btn_settings.pack(side=ctk.BOTTOM, fill='x', padx=10, pady=0)
        btn_settings.bind("<Enter>", lambda event, btn=btn_settings, select=True: hover_info(event, btn, select))
        btn_settings.bind("<Leave>", lambda event, btn=btn_settings, select=False: hover_info(event, btn, select))

        btn_news = ctk.CTkButton(master=sideFrame, image=news_img, text="", width=80, height=60, compound="right",
                                 fg_color=cp.blue, cursor="hand2",
                                 command=lambda: [])
        btn_news.pack(side=ctk.BOTTOM, fill='x', padx=10, pady=20)
        btn_news.bind("<Enter>", lambda event, btn=btn_news, select=True: hover_info(event, btn, select))
        btn_news.bind("<Leave>", lambda event, btn=btn_news, select=False: hover_info(event, btn, select))

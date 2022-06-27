import customtkinter as ctk
import Colorpalet as cp
import threading
import Data as data
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure


class GraphFrame(ctk.CTkFrame):
    stop = 0
    toggleBar = 0

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

        def start_refresh(state):
            data.get_state(state)
            btn1.configure(cursor="arrow", state="disabled")
            self.stop = 0
            live_graph()

        def load_graph(target):
            data.get_state(target)
            plot1.clear()
            # plot1.set_ylim(ymin=0, ymax=30)
            canvas1.draw()
            canvas1.get_tk_widget().pack(side=ctk.TOP, fill='x', padx=40, pady=40)

        def live_graph():
            if self.stop == 1:
                plot1.clear()
                btn1.configure(cursor="hand2", state="normal")
                self.stop = 0
            else:
                threading.Thread(target=data.get_live_data()).start()
                plot1.clear()
                plot1.plot(data.current_x, data.current_y)
                # plot1.set_ylim(ymin=0, ymax=30)
                canvas1.draw()
                canvas1.get_tk_widget().pack(side=ctk.TOP, fill='x', padx=40, pady=40)
                master.after(10000, lambda: [live_graph()])

        #----------Graph Frame----------
        graphFrame = ctk.CTkFrame(master=master, fg_color=cp.lightGrey, corner_radius=10)
        graphFrame.grid(row=0, column=1, sticky="nswe", pady=20, padx=20)

        tabBar = ctk.CTkFrame(graphFrame, fg_color=cp.darkGrey, border_color=cp.darkGrey)
        tabBar.pack(side=ctk.TOP, padx=40, pady=10)
        btn1 = ctk.CTkButton(tabBar, corner_radius=0, text="LIVE", width=100, hover_color=cp.darkGrey,
                             fg_color=cp.darkGrey, command=lambda: [select_button(btn1), start_refresh(0)])
        btn1.pack(side=ctk.LEFT)
        btn2 = ctk.CTkButton(tabBar, corner_radius=0, text="TODAY", width=100, hover_color=cp.darkGrey,
                             fg_color=cp.lightGrey, command=lambda: [select_button(btn2), load_graph(1)])
        btn2.pack(side=ctk.LEFT)
        btn3 = ctk.CTkButton(tabBar, corner_radius=0, text="24-HOURS", width=100, hover_color=cp.darkGrey,
                             fg_color=cp.lightGrey, command=lambda: [select_button(btn3), load_graph(2)])
        btn3.pack(side=ctk.LEFT)
        btn4 = ctk.CTkButton(tabBar, corner_radius=0, text="1-WEEK", width=100, hover_color=cp.darkGrey,
                             fg_color=cp.lightGrey, command=lambda: [select_button(btn4), load_graph(3)])
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

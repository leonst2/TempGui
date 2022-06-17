import customtkinter as ctk
import Colorpalet as cp
import threading
import Data as data
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure


class GraphFrame(ctk.CTkFrame):
    stop = False
    value_select = 0

    def __init__(self, master):
        super().__init__(master)

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

        def live_graph_temp():
            btn1.configure(cursor="arrow", state="disabled")
            self.stop = True
            load_graph(data.axes_x, data.temp_y)

        def stop_refresh():
            if self.stop:
                data.temp_y.clear()
                data.axes_x.clear()
                btn1.configure(cursor="hand2", state="normal")
                self.stop = False
                print("Stopped live refresh")

        def load_graph(x_axes, y_axes):
            if self.stop:
                threading.Thread(target=data.get_live_data()).start()
                plot1.clear()
                plot1.plot(x_axes, y_axes)
                # plot1.set_ylim(ymin=0, ymax=30)
                canvas1.draw()
                canvas1.get_tk_widget().pack(side=ctk.TOP, fill='x', padx=40, pady=40)
                master.after(10000, load_graph(x_axes, y_axes))
            else:
                print("Stopped progress!")
                self.stop = True

        def get_selected_value():
            if self.value_select == 0:
                print("all data")

            if self.value_select == 1:
                print("temperature")

            if self.value_select == 2:
                print("pressure")

            if self.value_select == 3:
                print("humidity")

            if self.value_select == 4:
                print("list view")

        graphFrame = ctk.CTkFrame(master=master, fg_color=cp.lightGrey, corner_radius=10)
        graphFrame.grid(row=0, column=1, sticky="nswe", padx=20, pady=20)

        tabBar = ctk.CTkFrame(graphFrame, fg_color=cp.darkGrey, border_color=cp.darkGrey)
        tabBar.pack(side=ctk.TOP, padx=40, pady=10)
        btn1 = ctk.CTkButton(tabBar, corner_radius=0, text="LIVE", width=100, hover_color=cp.darkGrey,
                             fg_color=cp.darkGrey, command=lambda: [select_button(btn1), live_graph_temp()])
        btn1.pack(side=ctk.LEFT)
        btn2 = ctk.CTkButton(tabBar, corner_radius=0, text="TODAY", width=100, hover_color=cp.darkGrey,
                             fg_color=cp.lightGrey, command=lambda: [select_button(btn2), stop_refresh()])
        btn2.pack(side=ctk.LEFT)
        btn3 = ctk.CTkButton(tabBar, corner_radius=0, text="24-HOURS", width=100, hover_color=cp.darkGrey,
                             fg_color=cp.lightGrey, command=lambda: [select_button(btn3), stop_refresh()])
        btn3.pack(side=ctk.LEFT)
        btn4 = ctk.CTkButton(tabBar, corner_radius=0, text="1-WEEK", width=100, hover_color=cp.darkGrey,
                             fg_color=cp.lightGrey, command=lambda: [select_button(btn4), stop_refresh()])
        btn4.pack(side=ctk.LEFT)

        fig = Figure(figsize=(16, 9))
        plot1 = fig.add_subplot(111)
        plot1.plot([], [])
        canvas1 = FigureCanvasTkAgg(fig, graphFrame)
        canvas1.draw()
        canvas1.get_tk_widget().pack(side=ctk.TOP, fill='x', padx=40, pady=40)

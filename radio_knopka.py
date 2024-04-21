from tkinter import *
from tkinter import ttk
class rad_button_class():
    def __init__(self,regime): 
        self.regime=regime
    def give_regime(self):
        return self.regime.get()
    def make_rad_btn(self):
        calc="Калькулятор"
        rect="Прямоугольник"
        position = {"padx":6, "pady":6, "anchor":NW}
        header=ttk.Label(text="Режим работы")
        header.pack(**position)
        calc_button=ttk.Radiobutton(text=calc,value=calc,variable=self.regime)
        calc_button.pack(**position)
        rect_button=ttk.Radiobutton(text=rect,value=rect,variable=self.regime)
        rect_button.pack(**position)




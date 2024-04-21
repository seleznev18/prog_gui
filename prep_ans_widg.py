from tkinter import *
from tkinter import ttk
class class_make_preparations(object):
    def do_prep(self):
        self.add_lbl=ttk.Label(text="Сложение")
        self.add_lbl.place(x=150,y=75)
        self.add_val=ttk.Label(text="0")
        self.add_val.place(x=150,y=100)
        self.subst_lbl=ttk.Label(text="Вычитание")
        self.subst_lbl.place(x=225,y=75)
        self.subst_val=ttk.Label(text="0")
        self.subst_val.place(x=225,y=100)
        self.mult_lbl=ttk.Label(text="Умножение")
        self.mult_lbl.place(x=300,y=75)
        self.mult_val=ttk.Label(text="0")
        self.mult_val.place(x=300,y=100)
        self.div_lbl=ttk.Label(text="Деление")
        self.div_lbl.place(x=375,y=75)
        self.div_val=ttk.Label(text="0")
        self.div_val.place(x=375,y=100)
        self.area_lbl=ttk.Label(text="Площадь")
        self.area_lbl.place(x=150,y=75)
        self.area_val=ttk.Label(text="0")
        self.area_val.place(x=150,y=100)
        self.perim_lbl=ttk.Label(text="Периметр")
        self.perim_lbl.place(x=225,y=75)
        self.perim_val=ttk.Label(text="0")
        self.perim_val.place(x=225,y=100)
        self.canv_rect=Canvas(bg="red",width=1,height=1)
        self.canv_rect.place(x=150,y=175)
        self.canv_lbl=Label(text="Прямоугольник по введенным данным")
        self.canv_lbl.place(x=150,y=150)
        self.error_lbl=Label(text="Ошибка ввода")
        self.error_lbl.place(x=350,y=50)







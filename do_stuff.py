from tkinter import *
from tkinter import ttk
import prep_ans_widg
class class_stuff(prep_ans_widg.class_make_preparations):
    def __init__(self,root,at1,at2,prp=prep_ans_widg.class_make_preparations()):
        self.root=root
        self.at1=at1
        self.at2=at2
        self.prp=prp
    def prep_calc(self):
        self.prp.do_prep()
        self.prp.area_lbl.destroy()
        self.prp.area_val.destroy()
        self.prp.perim_lbl.destroy()
        self.prp.perim_val.destroy()
        self.prp.canv_rect.destroy()
        self.prp.canv_lbl.destroy()
        self.prp.error_lbl.destroy()
    def prep_rect(self):
        self.prp.do_prep()
        self.prp.add_lbl.destroy()
        self.prp.add_val.destroy()
        self.prp.subst_lbl.destroy()
        self.prp.subst_val.destroy()
        self.prp.mult_lbl.destroy()
        self.prp.mult_val.destroy()
        self.prp.div_lbl.destroy()
        self.prp.div_val.destroy()
        self.prp.error_lbl.destroy()
    def prep_rect_too_big(self):
        self.prp.do_prep()
        self.prp.add_lbl.destroy()
        self.prp.add_val.destroy()
        self.prp.subst_lbl.destroy()
        self.prp.subst_val.destroy()
        self.prp.mult_lbl.destroy()
        self.prp.mult_val.destroy()
        self.prp.div_lbl.destroy()
        self.prp.div_val.destroy()
        self.prp.canv_rect.destroy()
        self.prp.canv_lbl.destroy()
    def dstr(self):
        self.prp.area_lbl.destroy()
        self.prp.area_val.destroy()
        self.prp.perim_lbl.destroy()
        self.prp.perim_val.destroy()
        self.prp.add_lbl.destroy()
        self.prp.add_val.destroy()
        self.prp.subst_lbl.destroy()
        self.prp.subst_val.destroy()
        self.prp.mult_lbl.destroy()
        self.prp.mult_val.destroy()
        self.prp.div_lbl.destroy()
        self.prp.div_val.destroy()
        self.prp.canv_rect.destroy()
        self.prp.canv_lbl.destroy()
        self.prp.error_lbl.destroy()
    def make_calc(self):
        self.prp.add_val.config(text=f"{round((self.at1+self.at2),2)}")
        self.prp.subst_val.config(text=f"{round((self.at1-self.at2),2)}")
        self.prp.mult_val.config(text=f"{round((self.at1*self.at2),2)}")
        if (self.at2==0):
            self.prp.div_val.config(text=f"Ошибка ввода")
        else:
            self.prp.div_val.config(text=f"{round((self.at1/self.at2),2)}")
    def make_rect(self):
        self.prp.area_val.config(text=f"{round((self.at1*self.at2),2)}")
        self.prp.perim_val.config(text=f"{round((self.at1*2+self.at2*2),2)}")
        self.prp.canv_rect.config(width=self.at1,height=self.at2)
    def make_rect_too_big(self):
        self.prp.area_val.config(text=f"{round((self.at1*self.at2),2)}")
        self.prp.perim_val.config(text=f"{round((self.at1*2+self.at2*2),2)}")
        self.prp.error_lbl.config(text="Слишком большие данные")
    def make_error(self):
        self.prp.do_prep()
        self.prp.error_lbl.config(text="Ошибка ввода")
        self.prp.area_lbl.destroy()
        self.prp.area_val.destroy()
        self.prp.perim_lbl.destroy()
        self.prp.perim_val.destroy()
        self.prp.add_lbl.destroy()
        self.prp.add_val.destroy()
        self.prp.subst_lbl.destroy()
        self.prp.subst_val.destroy()
        self.prp.mult_lbl.destroy()
        self.prp.mult_val.destroy()
        self.prp.div_lbl.destroy()
        self.prp.div_val.destroy()
        self.prp.canv_rect.destroy()
        self.prp.canv_lbl.destroy()


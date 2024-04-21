from tkinter import *
from tkinter import ttk
class attributes_button(object):
    def __init__(self,px,py,root):
        self.px=px
        self.py=py
        self.root=root
    def make_attr_btn(self):
        self.attr_btn=ttk.Entry(justify=RIGHT,width=10)
        self.attr_btn.place(x=self.px,y=self.py)
    def clear_attr(self):
        self.attr_btn.delete(0,END)

        
    
    




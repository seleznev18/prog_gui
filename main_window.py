from tkinter import *
from tkinter import ttk
import radio_knopka
import entry_knopka
import prep_ans_widg
import do_stuff
import input_check
root=Tk()
root.option_add("*tearOff", FALSE)
root.geometry("700x700")
root.title("Графический калькулятор")
default_regime=StringVar(value="Калькулятор")
regime_turner=radio_knopka.rad_button_class(default_regime)
regime_turner.make_rad_btn()
at1_name=ttk.Label(text="Атрибут 1")
at1_name.place(x=150,y=25)
at1=entry_knopka.attributes_button(150,50,root)
at1.make_attr_btn()
at2_name=ttk.Label(text="Атрибут 2")
at2_name.place(x=250,y=25)
at2=entry_knopka.attributes_button(250,50,root)
at2.make_attr_btn()
done_first=False
mode=0
def finish_wondow():
    global root
    root.destroy()
def clear_attr():
    global at1,at2
    at1.clear_attr()
    at2.clear_attr()
def switch_attr():
    global at1,at2,at1_name,at2_name,mode
    buff=at1
    at1=at2
    at2=buff
    if (mode==0):
        at1_name.config(text="Атрибут 2")
        at2_name.config(text="Атрибут 1")
        mode=1
    else:
        at1_name.config(text="Атрибут 1")
        at2_name.config(text="Атрибут 2")
        mode=0
def info_window():
    wnd=Tk() 
    wnd.title="Информация о приложении"
    wnd.geometry="500x500"
    wnd_text=ttk.Label(wnd,text="Данный калькулятор сделан при помощи Третьего рейха, Слава Сатане!666")
    wnd_text.pack(anchor=CENTER)
    wnd.mainloop()
def Start():
    curr_reg=regime_turner.give_regime()
    ch1=input_check.class_check(at1.attr_btn.get())
    ch2=input_check.class_check(at2.attr_btn.get())
    global done_first
    if ((curr_reg=="Калькулятор" and (ch1.do_check_calc()==False or ch2.do_check_calc()==False)) or (curr_reg=="Прямоугольник" and (ch1.do_check_rect()==False or ch2.do_check_rect()==False))):
        clc=do_stuff.class_stuff(root,at1.attr_btn.get(),at2.attr_btn.get())
        if (done_first==True):
            clc.dstr()
        clc.make_error()
        done_first=True
    else:
        clc=do_stuff.class_stuff(root,float(at1.attr_btn.get()),float(at2.attr_btn.get()))
        if (curr_reg=="Калькулятор"):
            if (done_first==True):
                clc.dstr()
            clc.prep_calc()
            clc.make_calc()
            done_first=True
        elif (curr_reg=="Прямоугольник" and float(at1.attr_btn.get())>0 and float(at2.attr_btn.get())>0):
            if (done_first==True):
                clc.dstr()
            if (float(at1.attr_btn.get())>300 or float(at2.attr_btn.get())>300):
                clc.prep_rect_too_big()
                clc.make_rect_too_big()
            else:
                clc.prep_rect()
                clc.make_rect()
            done_first=True
st_btn=ttk.Button(text="Выполнить вычисления",command=Start,width=23)
st_btn.place(x=350,y=25)
switch_attr_btn=ttk.Button(text="Поменять аргументы местами",command=switch_attr)
switch_attr_btn.place(x=150,y=0)
clear_btn=ttk.Button(text="Очистить атрибуты",command=clear_attr,width=23)
clear_btn.place(x=350,y=0)
end_btn=ttk.Button(text="ВЫХОД ИЗ ПРИЛОЖЕНИЯ",command=finish_wondow)
end_btn.place(x=500,y=0)
main_menu=Menu()
file_menu=Menu()
ops_menu=Menu()
info_menu=Menu()
file_menu.add_command(label="Выход из приложения",command=finish_wondow)
ops_menu.add_command(label="Очистить аргументы",command=clear_attr)
ops_menu.add_command(label="Выполнить операции",command=Start)
info_menu.add_command(label="Информация о программе",command=info_window)
main_menu.add_cascade(label="Файл",menu=file_menu)
main_menu.add_cascade(label="Операции",menu=ops_menu)
main_menu.add_cascade(label="Справка",menu=info_menu)
root.config(menu=main_menu)
root.mainloop()





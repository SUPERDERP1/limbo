from tkinter import *
import random as r
import time as t
correct = r.randint(1,8)
win = Tk() 
win.geometry("1440x900") 
def gstart():
    key1 = Toplevel(win,bg="red")
    key2 = Toplevel(win,bg="red")
    key3 = Toplevel(win,bg="red")
    key4 = Toplevel(win,bg="red")
    key5 = Toplevel(win,bg="red")
    key6 = Toplevel(win,bg="red")
    key7 = Toplevel(win,bg="red")
    key8 = Toplevel(win,bg="red")
    key1.geometry("+172+150")
    key2.geometry("+472+150")
    key3.geometry("+772+150")
    key4.geometry("+1072+150")
    key5.geometry("+172+450")
    key6.geometry("+472+450")
    key7.geometry("+772+450")
    key8.geometry("+1072+450")
    win.iconify()
    t.sleep(5)
    match correct:
        case 1:
            key1.config(bg="green")
            key1.update()
            t.sleep(1)
            key1.config(bg="red")
        case 2:
            key2.config(bg="green")
            key2.update()
            t.sleep(1)
            key2.config(bg="red")
        case 3:
            key3.config(bg="green")
            key3.update()
            t.sleep(1)
            key3.config(bg="red")
        case 4:
            key4.config(bg="green")
            key4.update()
            t.sleep(1)
            key4.config(bg="red")
        case 5:
            key5.config(bg="green")
            key5.update()
            t.sleep(1)
            key5.config(bg="red")
        case 6:
            key6.config(bg="green")
            key6.update()
            t.sleep(1)
            key6.config(bg="red")
        case 7:
            key7.config(bg="green")
            key7.update()
            t.sleep(1)
            key7.config(bg="red")
        case 8:
            key8.config(bg="green")
            key8.update()
            t.sleep(1)
            key8.config(bg="red")
start = Button(
    text="start",
    command=gstart
)
start.pack()
win.mainloop() 

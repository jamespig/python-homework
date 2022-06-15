from tkinter import *
import time
from random import *
from PIL import ImageTk, Image
from tkinter import messagebox

tk=Tk()
tk.title("Through The River")

class Rect:
    def __init__(self, canvas, color, winW, winH, starX, starY, x1, y1, x2, y2, t):
        self.canvas=canvas
        self.id=canvas.create_rectangle(x1, y1, x2, y2, fill=color, dash=(5, 1), tag=t)
        self.canvas.move(self.id, starX, starY)
        self.x=step
        self.y=0
        self.canvas.move(self.id, self.x, self.y)
        rectPos=self.canvas.coords(self.id)

winW=1500
winH=500
step=5

canvas=Canvas(tk, width=winW, height=winH)

canvas.pack()
tk.update()

boat=Rect(canvas, 'brown', winW, winH, starX=10, starY=300, x1=10, y1=50, x2=260, y2=80, t='b')

sheepUR=Rect(canvas, 'light gray', winW, winH, starX=10, starY=50, x1=10, y1=50, x2=60, y2=100, t='sheepUR')
wolfUR=Rect(canvas, 'gray', winW, winH, starX=80, starY=50, x1=10, y1=50, x2=60, y2=100, t='wolfUR')
vegetUR=Rect(canvas, 'light green', winW, winH, starX=150, starY=50, x1=10, y1=50, x2=60, y2=100, t='vegetUR')

sheepUL=Rect(canvas, '', winW, winH, starX=winW-220, starY=50, x1=10, y1=50, x2=60, y2=100, t='sheepUL')
wolfUL=Rect(canvas, '', winW, winH, starX=winW-150, starY=50, x1=10, y1=50, x2=60, y2=100, t='wolfUL')
vegetUL=Rect(canvas, '', winW, winH, starX=winW-80, starY=50, x1=10, y1=50, x2=60, y2=100, t='vegetUL')
'''
------------------------------------------------------------------------------------------------------------------------------
'''
boatR=True
baotL=False

sheepDExist=False
wolfDExist=False
vegetDExist=False

sheepURExist=True
wolfURExist=True
vegetURExist=True

sheepULExist=False
wolfULExist=False
vegetULExist=False
'''
------------------------------------------------------------------------------------------------------------------------------
'''
def appearright():
    global boatR
    global boatL
    boatR=False
    boatL=True
    canvas.delete('b')
    boat=Rect(canvas, 'brown', winW, winH, starX=winW-280, starY=300, x1=10, y1=50, x2=260, y2=80, t='b')
    if sheepURExist == True and wolfURExist == True and vegetURExist == False:
        if vegetULExist == False:
            canvas.delete('vegetD')
            vegetD=Rect(canvas, 'light green', winW, winH, starX=winW-80, starY=250, x1=10, y1=50, x2=60, y2=100, t='vegetD')
        messagebox.showerror('出事啦!', '羊被狼吃掉了!!!')
        boatR=True
        boatL=False
        canvas.delete('b')
        boat=Rect(canvas, 'brown', winW, winH, starX=10, starY=300, x1=10, y1=50, x2=260, y2=80, t='b')
        canvas.delete('vegetD')
        vegetD=Rect(canvas, 'light green', winW, winH, starX=190, starY=250, x1=10, y1=50, x2=60, y2=100, t='vegetD')
    elif sheepURExist == True and wolfURExist == False and vegetURExist == True:
        if wolfULExist == False:
            canvas.delete('wolfD')
            wolfD=Rect(canvas, 'gray', winW, winH, starX=winW-150, starY=250, x1=10, y1=50, x2=60, y2=100, t='wolfD')
        messagebox.showerror('出事啦!', '菜被羊吃掉了!!!')
        boatR=True
        boatL=False
        canvas.delete('b')
        boat=Rect(canvas, 'brown', winW, winH, starX=10, starY=300, x1=10, y1=50, x2=260, y2=80, t='b')
        canvas.delete('wolfD')
        wolfD=Rect(canvas, 'gray', winW, winH, starX=120, starY=250, x1=10, y1=50, x2=60, y2=100, t='wolfD')
    else:
        if sheepDExist == True:
            canvas.delete('sheepD')
            sheepD=Rect(canvas, 'light gray', winW, winH, starX=winW-220, starY=250, x1=10, y1=50, x2=60, y2=100, t='sheepD')
        if wolfDExist == True:
            canvas.delete('wolfD')
            wolfD=Rect(canvas, 'gray', winW, winH, starX=winW-150, starY=250, x1=10, y1=50, x2=60, y2=100, t='wolfD')
        if vegetDExist == True:
            canvas.delete('vegetD')
            vegetD=Rect(canvas, 'light green', winW, winH, starX=winW-80, starY=250, x1=10, y1=50, x2=60, y2=100, t='vegetD')
def appearleft():
    global boatR
    global boatL
    boatR=True
    boatL=False
    canvas.delete('b')
    boat=Rect(canvas, 'brown', winW, winH, starX=10, starY=300, x1=10, y1=50, x2=260, y2=80, t='b')
    if sheepULExist == True and wolfULExist == True and vegetULExist == False:
        if vegetURExist == False:
            canvas.delete('vegetD')
            vegetD=Rect(canvas, 'light green', winW, winH, starX=190, starY=250, x1=10, y1=50, x2=60, y2=100, t='vegetD')
        messagebox.showerror('出事啦!', '羊被狼吃掉了!!!')
        boatR=False
        boatL=True
        canvas.delete('b')
        boat=Rect(canvas, 'brown', winW, winH, starX=winW-280, starY=300, x1=10, y1=50, x2=260, y2=80, t='b')
    elif sheepULExist == True and wolfULExist == False and vegetULExist == True:
        if wolfURExist == False:
            canvas.delete('wolfD')
            wolfD=Rect(canvas, 'gray', winW, winH, starX=120, starY=250, x1=10, y1=50, x2=60, y2=100, t='wolfD')
        messagebox.showerror('出事啦!', '菜被羊吃掉了!!!')
        boatR=False
        boatL=True
        canvas.delete('b')
        boat=Rect(canvas, 'brown', winW, winH, starX=winW-280, starY=300, x1=10, y1=50, x2=260, y2=80, t='b')
    else:
        if sheepDExist == True:
            canvas.delete('sheepD')
            sheepD=Rect(canvas, 'light gray', winW, winH, starX=50, starY=250, x1=10, y1=50, x2=60, y2=100, t='sheepD')
        if wolfDExist == True:
            canvas.delete('wolfD')
            wolfD=Rect(canvas, 'gray', winW, winH, starX=120, starY=250, x1=10, y1=50, x2=60, y2=100, t='wolfD')
        if vegetDExist == True:
            canvas.delete('vegetD')
            vegetD=Rect(canvas, 'light green', winW, winH, starX=190, starY=250, x1=10, y1=50, x2=60, y2=100, t='vegetD')
'''
------------------------------------------------------------------------------------------------------------------------------
'''    
def sheepMR():
    global sheepDExist
    global sheepURExist
    global wolfDExist
    global vegetDExist
    global boatR
    if wolfDExist == True or vegetDExist == True:
        messagebox.showwarning('乘載量警告','放不下了啦!')
    else:
        if sheepDExist == False and sheepURExist == True and boatR == True:
            canvas.delete('sheepUR')
            sheepUR=Rect(canvas, '', winW, winH, starX=10, starY=50, x1=10, y1=50, x2=60, y2=100, t='sheepUR')
            sheepD=Rect(canvas, 'light gray', winW, winH, starX=50, starY=250, x1=10, y1=50, x2=60, y2=100, t='sheepD')
            sheepDExist=True
            sheepURExist=False
        elif sheepDExist == True and sheepURExist == False and boatR == True:
            canvas.delete('sheepD')
            sheepUR=Rect(canvas, 'light gray', winW, winH, starX=10, starY=50, x1=10, y1=50, x2=60, y2=100, t='sheepUR')
            sheepDExist=False
            sheepURExist=True
def wolfMR():
    global wolfDExist
    global wolfURExist
    global sheepDExist
    global vegetDExist
    global boatR
    if sheepDExist == True or vegetDExist == True:
        messagebox.showwarning('乘載量警告','放不下了啦!')
    else:
        if wolfDExist == False and wolfURExist == True and boatR == True:
            canvas.delete('wolfUR')
            wolfUR=Rect(canvas, '', winW, winH, starX=80, starY=50, x1=10, y1=50, x2=60, y2=100, t='wolfUR')
            wolfD=Rect(canvas, 'gray', winW, winH, starX=120, starY=250, x1=10, y1=50, x2=60, y2=100, t='wolfD')
            wolfDExist=True
            wolfURExist=False
        elif wolfDExist == True and wolfURExist == False and boatR == True:
            canvas.delete('wolfD')
            wolfUR=Rect(canvas, 'gray', winW, winH, starX=80, starY=50, x1=10, y1=50, x2=60, y2=100, t='wolfUR')
            wolfDExist=False
            wolfURExist=True
def vetgetMR():
    global vegetDExist
    global vegetURExist
    global sheepDExist
    global wolfDExist
    global boatR
    if sheepDExist == True or wolfDExist == True:
        messagebox.showwarning('乘載量警告','放不下了啦!')
    else:
        if vegetDExist == False and vegetURExist == True and boatR == True:
            canvas.delete('vegetUR')
            vegetUR=Rect(canvas, '', winW, winH, starX=150, starY=50, x1=10, y1=50, x2=60, y2=100, t='vegetUR')
            vegetD=Rect(canvas, 'light green', winW, winH, starX=190, starY=250, x1=10, y1=50, x2=60, y2=100, t='vegetD')
            vegetDExist=True
            vegetURExist=False
        elif vegetDExist == True and vegetURExist == False and boatR == True:
            canvas.delete('vegetD')
            vegetUR=Rect(canvas, 'light green', winW, winH, starX=150, starY=50, x1=10, y1=50, x2=60, y2=100, t='vegetUR')
            vegetDExist=False
            vegetURExist=True
'''
------------------------------------------------------------------------------------------------------------------------------
'''
def win():
    if sheepULExist == True and wolfULExist == True and vegetULExist == True:
        messagebox.showinfo('獲勝!', '恭喜你贏得遊戲!!!')
        tk.destroy()
'''
------------------------------------------------------------------------------------------------------------------------------
'''    
def sheepML():
    global sheepDExist
    global sheepULExist
    global wolfDExist
    global vegetDExist
    global boatL
    if sheepDExist == True and sheepULExist == False and boatL == True:
        canvas.delete('sheepUL')
        canvas.delete('sheepD')
        sheepUL=Rect(canvas, 'light gray', winW, winH, starX=winW-220, starY=50, x1=10, y1=50, x2=60, y2=100, t='sheepUL')
        sheepDExist=False
        sheepULExist=True
    elif sheepDExist == False and sheepULExist == True and boatL == True:
        if wolfDExist == True or vegetDExist == True:
            messagebox.showwarning('乘載量警告','放不下了啦!')
        else:
            canvas.delete('sheepUL')
            sheepUL=Rect(canvas, '', winW, winH, starX=winW-220, starY=50, x1=10, y1=50, x2=60, y2=100, t='sheepUL')
            sheepD=Rect(canvas, 'light gray', winW, winH, starX=winW-220, starY=250, x1=10, y1=50, x2=60, y2=100, t='sheepD')
            sheepDExist=True
            sheepULExist=False
    win()
def wolfML():
    global wolfDExist
    global wolfULExist
    global sheepDExist
    global vegetDExist
    global boatL
    if wolfDExist == True and wolfULExist == False and boatL == True:
        canvas.delete('wolfUL')
        canvas.delete('wolfD')
        wolfUL=Rect(canvas, 'gray', winW, winH, starX=winW-150, starY=50, x1=10, y1=50, x2=60, y2=100, t='wolfUL')
        wolfDExist=False
        wolfULExist=True
    elif wolfDExist == False and wolfULExist == True and boatL == True:
        if sheepDExist == True or vegetDExist == True:
            messagebox.showwarning('乘載量警告','放不下了啦!')
        else:
            canvas.delete('wolfUL')
            wolfUL=Rect(canvas, '', winW, winH, starX=winW-150, starY=50, x1=10, y1=50, x2=60, y2=100, t='wolfUL')
            wolfD=Rect(canvas, 'gray', winW, winH, starX=winW-150, starY=250, x1=10, y1=50, x2=60, y2=100, t='wolfD')
            wolfDExist=True
            wolfULExist=False
    win()
def vetgetML():
    global vegetDExist
    global vegetULExist
    global sheepDExist
    global wolfDExist
    global boatL
    if vegetDExist == True and vegetULExist == False and boatL == True:
        canvas.delete('vegetUL')
        canvas.delete('vegetD')
        vegetUL=Rect(canvas, 'light green', winW, winH, starX=winW-80, starY=50, x1=10, y1=50, x2=60, y2=100, t='vegetUL')
        vegetDExist=False
        vegetULExist=True
    elif vegetDExist == False and vegetULExist == True and boatL == True:
        if sheepDExist == True or vegetDExist == True:
            messagebox.showwarning('乘載量警告','放不下了啦!')
        else:
            canvas.delete('vegetUL')
            vegetUL=Rect(canvas, '', winW, winH, starX=winW-80, starY=50, x1=10, y1=50, x2=60, y2=100, t='vegetUL')
            vegetD=Rect(canvas, 'light green', winW, winH, starX=winW-80, starY=250, x1=10, y1=50, x2=60, y2=100, t='vegetD')
            vegetDExist=True
            vegetULExist=False
    win()
'''
------------------------------------------------------------------------------------------------------------------------------
'''
sheepbtnR=Button(tk, text='Sheep', height=1, width=6, command=sheepMR).place(x=20, y=50)
wolfbtnR=Button(tk, text='Wolf', height=1, width=6, command=wolfMR).place(x=90, y=50)
vegetbtnR=Button(tk, text='Vegetable', height=1, width=8, command=vetgetMR).place(x=160, y=50)

sheepbtnL=Button(tk, text='Sheep', height=1, width=6, command=sheepML).place(x=winW-220, y=50)
wolfbtnL=Button(tk, text='Wolf', height=1, width=6, command=wolfML).place(x=winW-150, y=50)
vegetbtnL=Button(tk, text='Vegetable', height=1, width=8, command=vetgetML).place(x=winW-80, y=50)
'''
------------------------------------------------------------------------------------------------------------------------------
'''  
rightbtn=Button(tk, text="Right", command=appearright, height=1, width=5)
leftbtn=Button(tk, text="Left", command=appearleft, height=1, width=5)
'''
------------------------------------------------------------------------------------------------------------------------------
'''  
leftbtn.pack(anchor=N, side=LEFT, padx=5)
rightbtn.pack(anchor=N, side=LEFT)
    
tk.mainloop()
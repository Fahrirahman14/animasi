from tkinter import *
import time
import math

lebar = 1200
tinggi = 700

class adr(object):

     lWidth = lebar
     lHeight = tinggi

     px = 50
     py = 200
     
     def __init__(self):

        self.root = Tk()
        self.root.title("Animasi Pantul Bola")
        self.canvas = Canvas(self.root, width=self.lWidth, height = self.lHeight, bg='black')
        self.canvas.pack()
        self.alien2 = self.canvas.create_oval(self.px, self.py, self.px+50, self.py+50, outline='lightgreen', fill='lightblue')
        self.canvas.pack()
        self.root.after(0, self.animation)
        self.root.mainloop()
        
     def animation(self):
        x = 2
        xn = 0.5
        y = 0

        while True:
            yold = y
            y = x * 4 - 7**2 + 20
               
            yhasil = y - yold
            x = x + xn
            
            time.sleep(0.015)
            self.canvas.move(self.alien2, x, y)
            self.canvas.update()
            pos = self.canvas.coords(self.alien2)

            print ("y : "+str(y)+" - x : "+str(x))
                
            if pos[3] >= 600 or pos[1] <= 0:
                x = 2
                y = 0

adr()

from random import randrange as rnd, choice
import tkinter as tk
from tkinter import*
import math
import time


root = tk.Tk()
root.geometry('885x558')
cosmos=Canvas(root, width=885,height=558,)

fon = PhotoImage(file="cosmos.png")

id_img= cosmos.create_image(0,0,anchor=NW,image=fon)

cosmos.pack(fill=BOTH,expand=1)
angle=0



class planet():
    def __init__(self):
        self.id = cosmos.create_oval(0,0,0,0)
        self.live=1
        
    def solnce(self):
        x=self.x=0
        y=self.y=558
        r=self.r=125
        color=self.color="yellow"
        cosmos.coords(self.id, x-r, y-r, x+r, y+r)
        cosmos.create_text(self.x+24,self.y-10,text='солнце')
        cosmos.itemconfig(self.id, fill=color)
        cosmos.tag_bind(self.id, '<Button-1>', planet.focIn)
      
        
    def mercury(self):
        x=self.x=0
        y=self.y=558
        r=self.r=20
        self.xn=0 #  !!!начало координат!!!
        self.yn=558 #!!! начало координат!!!
        self.rv=165 #!!! собственный радиус вращения!!!
        self.v=+1.0 # !!! скорость поворота 
        color=self.color="white"
        cosmos.coords(self.id, x-r, y-r, x+r, y+r)
        cosmos.itemconfig(self.id, fill=color) 
       
    def venera(self):
        x=self.x=0
        y=self.y=558
        r=self.r=30
        self.xn=0
        self.yn=558
        self.rv=225
        self.v=-2.2
        color=self.color="grey"
        cosmos.coords(self.id, x-r, y-r, x+r, y+r)
        cosmos.itemconfig(self.id, fill=color)       
    
    def earth(self):
        x=self.x=0
        y=self.y=558
        r=self.r=40
        self.xn=0
        self.yn=558
        self.rv=295
        self.v=-4.3
        color=self.color="blue"
        cosmos.coords(self.id, x-r, y-r, x+r, y+r)
        cosmos.itemconfig(self.id, fill=color)

    def mars(self):
        x=self.x=342
        y=self.y=279
        r=self.r=30
        self.xn=0
        self.yn=558
        self.rv=370
        self.v=-4.0
        color=self.color="red"
        cosmos.coords(self.id, x-r, y-r, x+r, y+r)
        cosmos.itemconfig(self.id, fill=color)
        cosmos.itemconfig(self.id, fill=color)
    def jupiter(self):
        x=self.x=342
        y=self.y=279
        r=self.r=60
        self.xn=0
        self.yn=558
        self.rv=460
        self.v=-6.4
        color=self.color="pink"
        cosmos.coords(self.id, x-r, y-r, x+r, y+r)
        cosmos.itemconfig(self.id, fill=color)
       
    def saturn(self):
        x=self.x=342
        y=self.y=279
        r=self.r=50
        self.xn=0
        self.yn=558
        self.rv=560
        self.v=-5.6
        color=self.color="sky blue"
        cosmos.coords(self.id, x-r, y-r, x+r, y+r)
        cosmos.itemconfig(self.id, fill=color)
        
    def uran (self):
        x=self.x=342
        y=self.y=279
        r=self.r=40
        self.xn=0
        self.yn=558
        self.rv=650
        self.v=-3.3
        color=self.color="deep sky blue"
        cosmos.coords(self.id, x-r, y-r, x+r, y+r)
        cosmos.itemconfig(self.id, fill=color)
             
    def neptun(self):
        x=self.x=342
        y=self.y=279
        r=self.r=40
        self.xn=0
        self.yn=558
        self.rv=700
        self.v=0
        color=self.color="medium blue"
        cosmos.coords(self.id, x-r, y-r, x+r, y+r)
        cosmos.itemconfig(self.id, fill=color)
             
        
    def set_coords(self):
        cosmos.coords(
                self.id,
                self.x - self.r,
                self.y - self.r,
                self.x + self.r,
                self.y + self.r
              )

    def move(self):
            global angle
            angle+=0.02
            if angle>=360:
                angle=0
            self.x =self.xn+ self.rv* math.sin(angle-self.v) 
            self.y =self.yn+ self.rv* math.cos(angle-self.v)
           # if 'self.txt' in globals():
               # cosmos.delete(1.0,self.txt)      !!!l дораб удаление текста
            self.txt=cosmos.create_text(self.x,self.y,text='меркурий')
            
           
            self.set_coords()   
    def focIn(event):
      okno=Frame(cosmos,width=100,height=558,bg="red")
      okno.pack(side=RIGHT,expand=1)
             
    


t1=planet()
t2=planet()
t3=planet()
t4=planet()
t5=planet()
t6=planet()
t7=planet()
t8=planet()
t9=planet()



def gotovo(event=''):
      global t1,t2,t3,t4,t5,t6,t7,t8,t9
      t1.solnce()
      t2.mercury()
      t3.venera()
      t4.earth()
      t5.mars()
      t6.jupiter()
      t7.saturn()
      t8.uran()
      t9.neptun()
      
      while t1.live:
          t2.move()
          t3.move()
          t4.move()
          t5.move()
          t6.move()
          t7.move()
          t8.move()
          t9.move()
          cosmos.update()
          time.sleep(0.1)
gotovo()       

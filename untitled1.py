from random import randrange as rnd, choice
import tkinter as tk
from tkinter import*
import math
import time


root = tk.Tk()
root.geometry('1024x576')
cosmos=Canvas(root, width=1024,height=576,highlightthickness=0)

fon = PhotoImage(file="black.png")
id_img= cosmos.create_image(0,0,anchor=NW,image=fon)

angle=0




merkury=Canvas(cosmos,width=70 ,height=38,highlightthickness=0)
merk=PhotoImage(file="merc.png",width=70,height=38)
id_img_merk=merkury.create_image(0,0,anchor =NW,image=merk)
merkury.place(x=10,y=10)



solnce=Canvas(cosmos,width=250 ,height=225,highlightthickness=0)
soln=PhotoImage(file="solnce.png",width=250,height=225)
id_img_sonlce=solnce.create_image(0,0,anchor =NW,image=soln)
solnce.place(x=0,y=355)
cosmos.pack(expand=True,fill=BOTH)
'''       
     

         def solnce(self):
        x=self.x=0
        y=self.y=558
        r=self.r=125
        color=self.color="yellow"
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
            self.set_coords()   
    def focIn(self,event):
      print('Focus')
      cosmos.itemconfig(self.id,fill='white')        
    


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
      global t1
      t1.merkury()
      
'''  
t1=1 
while t1==1:   
    cosmos.update()
    merkury.update()
    solnce.update()
    
'''     
gotovo()       '''
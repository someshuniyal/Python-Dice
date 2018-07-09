import random
from tkinter import *
from tkinter import font
import os
os.system("cls")

class dice(Frame):
    def __init__(self,root):
        super().__init__(root)
        self.place(x=0,y=0,width=300,height=300)
        self["bg"]="#e5e8e8"
        self.dice_font=font.Font(family="Arial",size=25)
        self.again_button()
        self.num_label()

    def effects(self):
        if self.effect_count>=1:
            self.effect_count-=1
            n=random.choice(self.list)
            self.num_var.set(n)
            self.list.remove(n)
            self.id=self.after(100,self.effects)
        else:
            self.num_var.set(random.randrange(1,7))
            self.button["state"]=NORMAL

    def event_handaler(self):
        self.list=[*range(1,7)]
        self.button_var.set("Again")
        self.effect_count=6
        self.num_font["size"]=50
        self.button["state"]=DISABLED
        self.effects()

    def num_label(self):
        self.num_var=StringVar()
        self.num_var.set("Genarate")
        self.num_font=font.Font(family="hooge 05_53",size=35)
        self.random_label=Label(self,bg="#e5e8e8",fg="#2e4053",font=self.num_font,textvariable=self.num_var)
        self.random_label.place(x=0,y=50,width=300,height=100)

    def again_button(self):
        self.button_var=StringVar()
        self.button_var.set("Start")
        self.button_font=font.Font(family="Arial",size=15)
        self.button=Button(self,bd=0,bg="#ec7063",activebackground="#ec7063",activeforeground="white",fg="white",font=self.button_font,textvariable=self.button_var,command=self.event_handaler)
        self.button.place(x=100,y=200,width=100,height=50)

root=Tk()
root.geometry("300x300")
root.resizable(width=False,height=False)
root.title("Random Genarator")
obj=dice(root)
root.mainloop()

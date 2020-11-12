import tkinter as t
from tkinter import *
#from src import sentiment_analyser #import *


class GUI:

    def __init__(self,root):
       # self.root = t.Tk()
       # self.root.title("Sentiment Analyser")
       # self.root.config(bg = "light grey")
       # self.root.resizable(False , False)

        self.frame1 = Frame(root ,height=500 , width=800)
        self.frame1.propagate(0)
        self.frame1.pack()

        self.l = Label(self.frame1, text="Welcome To Sentiment\nAnalyser")
        self.l.config(font=("Courier", 44))
        self.l.place(x=60, y=50, anchor="nw")
    # l.pack()

        self.l1 = Label(self.frame1, text = "Enter A Keyword :")
        self.l1.config(font=("Courier", 17))
        self.l1.place(x = 90 , y = 250 , anchor = "nw")

        self.e = Entry(self.frame1 , text="Keyword",width = 35 , font = ("Times new roman" , 15))
        self.e.place(x = 360 , y = 255 , anchor="nw")

        self.l2 = Label(self.frame1, text="Enter Count :")
        self.l2.config(font=("Courier", 17))
        self.l2.place(x=90, y=300, anchor="nw")

        self.e1 = Entry(self.frame1, text="Count", width=15, font=("Times new roman", 15))
        self.e1.place(x=360, y=300, anchor="nw")

    #x = str(e.get())
    #y = int(e1.get())

    #def printinfo():
        #print(x,y)

        self.b1 = Button(self.frame1, text="Search", height=2, width=10, command = self.onclick) #command = sentiment_analyser.main(x, y))
        self.b1.place(x=380, y=350, anchor="nw")

        self.b2 = Button(self.frame1, text="Exit", height=2, width=10, command=lambda:root.destroy())
        self.b2.place(x=490, y=350, anchor="nw")

        #root.mainloop()

    def onclick(self):
        x=self.e.get()
        y=self.e1.get()
        print("hello",x , y)

root=t.Tk()
f=GUI(root)
root.mainloop()
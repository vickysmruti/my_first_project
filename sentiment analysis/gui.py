import tkinter as t
from tkinter import *
#from PIL import ImageTk,Image
from src import sentiment_analyser, Image_search
#from src import visual

root = t.Tk()
root.title('Twitter Application')
root.configure(bg = 'light grey')
root.resizable(FALSE, FALSE)
#root.geometry("800x500")

frame = Frame(root, height=500, width=800)
frame.propagate(0)
#frame.place(x=0, y=0, anchor="nw", width=800, height=500)
frame.pack()

l = Label(frame , text="Welcome")
l.config(font=("Courier", 44))
l.place(x=280,y=50,anchor="nw")
#l.pack()

b1 = Button(frame, text = "Sentiment Analysis", height=2 , width=15,command=sentiment_analyser.main)
b1.place(x=250, y=250)

b2 = Button(frame, text = "Image Search", height=2 , width=15, command=Image_search.main)
b2.place(x=450, y=250)

b3 = Button(frame, text="Exit" , height=2 , width=10 , command = lambda:root.destroy())
b3.place(x=380,y=350)


root.mainloop()

import tweepy
from tweepy import OAuthHandler
import wget
import os
import tkinter as t
from tkinter import *
import urllib
import time

class GUI:
    def __init__(self, root):

        #self.root = t.Tk()
        #self.root.title("Image Search")
        #self.root.resizable(False, False)
        #self.root.config(bg = "grey")

        self.f = Frame(root, height=500, width=800)
        self.f.config(bg = "#99d8d0")
        self.f.propagate(0)
        self.f.pack()

        self.l = Label(self.f, text="Tag Based Image Search")
        self.l.config(font=("Courier", 38), bg = "#99d8d0")
        self.l.place(x=60, y=50, anchor="nw")

        self.l1 = Label(self.f, text="Enter Image Keyword :")
        self.l1.config(font=("Courier", 16), bg = "#99d8d0")
        self.l1.place(x=90, y=150, anchor='nw')

        self.e = Entry(self.f, text="Keyword", width=35, font=("Times new roman", 15))
        self.e.place(x=390, y=150)

        self.l2 = Label(self.f, text="Enter Limit :")
        self.l2.config(font=("Courier", 16), bg = "#99d8d0")
        self.l2.place(x=193, y=200, anchor="nw")

        self.e1 = Entry(self.f, text="Count", width=35, font=("Times new roman", 15))
        self.e1.place(x=390, y=200)

        #x = e.get()
        #y = e1.get()
        #print(x,y)

        self.b1 = Button(self.f, text="Search", height=2, width=10,
                     command=lambda: self.onclick())  # command =self.onclick)
        self.b1.place(x=390, y=250, anchor="nw")

        self.b2 = Button(self.f, text="Exit", height=2, width=10, command=lambda: root.destroy())
        self.b2.place(x=490, y=250, anchor="nw")


        #self.root.mainloop()

    def Create_Dir(self,dir_name):
        if not os.path.exists("data"):
            try:
                os.mkdir("data")
                print("Created directory 'data'")
            except:
                print("Unable to create directory 'data': Directory already exists")
        else:
            print("Unable to create directory 'data': Directory already exists")

        if not os.path.exists("data/data_" + dir_name):
            try:
                os.mkdir("data/data_" + dir_name)
                print("Created directory 'data/data_" + dir_name + "'")
            except:
                print("Unable to create directory 'data/data_" + dir_name + "': Directory already exists")
        else:
            print("Unable to create directory 'data/data_" + dir_name + "': Directory already exists")

        if not os.path.exists("data/data_" + dir_name + '/img'):
            try:
                os.mkdir("data/data_" + dir_name + '/img')
                print("Created directory 'data/data_" + dir_name + "/img'")
            except:
                print("Unable to create directory 'data/data_" + dir_name + "/img': Directory already exists")
        else:
            print("Unable to create directory 'data/data_" + dir_name + "/img': Directory already exists")



    def onclick(self):
        x = self.e.get()
        y = self.e1.get()
        #print(x,y)
        self.authen(x, y)

    def authen(self, x, y):

        row = 1
        self.Create_Dir(x)
        file_path = "data/data_" + x

        consumer_key = 'e9RuYkFI4EEcdxWmcacjxzgkA'
        consumer_secret = 'RQWE0QSUlUXhEGxy2mVoA83DQwxqq9v5KzeqTt95vcNeLN16gn'
        access_token = '1270244974366543874-BngXbjyLLyWkWQKW5xvPemVnL9tgzz'
        access_token_secret = 'cI967H4YmuMRNX8NoQZeuKbzoyhZ4lWL742HgOjvzVPEk'

        try:
            auth = OAuthHandler(consumer_key, consumer_secret)
            auth.set_access_token(access_token, access_token_secret)
            api = tweepy.API(auth)
            print("Successful")
        except:
            print("Error: Authentication Failed")

        tweets = api.search(q=x, count=y, lang='en')

        media_files = set()
        for status in tweets:
            media = status.entities.get('media', [])
            if (len(media) > 0):
                media_files.add(media[0]['media_url'])
        #s = []
        #for media_file in media_files:
            #s.append(wget.download(media_file))

        for src in media_files:
            try:
                #print("(" + str(row) + "/" + str(len(img_src)) + ") Images Downloaded")
                urllib.request.urlretrieve(src, file_path + '/img/Twitter_' + str(row) +".jpeg")
                row += 1
                time.sleep(1.5)
            except:
                print("Image Download Failed. Downloading next image")


#gui_image()
def main():
    root = t.Tk()
    g = GUI(root)
    root.mainloop()

main()
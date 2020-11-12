import tweepy
from tweepy import OAuthHandler
import textblob
from textblob import TextBlob
import re
import tkinter as t
from tkinter import *
import time
#import visual
import matplotlib.pyplot as plt
import pandas as p



class TweetClient(object):

    def __init__(self):
        consumer_key = 'e9RuYkFI4EEcdxWmcacjxzgkA'
        consumer_secret = 'RQWE0QSUlUXhEGxy2mVoA83DQwxqq9v5KzeqTt95vcNeLN16gn'
        access_token = '1270244974366543874-BngXbjyLLyWkWQKW5xvPemVnL9tgzz'
        access_token_secret = 'cI967H4YmuMRNX8NoQZeuKbzoyhZ4lWL742HgOjvzVPEk'


        try:
            self.auth = OAuthHandler(consumer_key, consumer_secret)
            self.auth.set_access_token(access_token, access_token_secret)
            self.api = tweepy.API(self.auth)
        except:
            print("Error: Authentication Failed")


    def clean_tweet(self, tweet):
        return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z\t]) | (\w+:\/\/\S+ )" , " ", tweet).split())


    def get_tweet_sentiment(self, tweet):
        analysis = TextBlob(self.clean_tweet(tweet))
    # set sentiment
        if analysis.sentiment.polarity > 0:
            return 'positive'
        elif analysis.sentiment.polarity == 0:
            return 'neutral'
        else:
            return 'negative'


    def get_tweets(self, query, count=10):
        tweets = []
        #fetched_tweets = []
        try:
            # call twitter api to fetch tweets
            fetched_tweets = self.api.search(q=query, count=count)
            #parsing tweets one by one
            for tweet in fetched_tweets:
                # empty dictionary to store required params of a tweet
                parsed_tweet = {}

                # saving text of tweet
                parsed_tweet['text'] = tweet.text
                # saving sentiment of tweet
                parsed_tweet['sentiment'] = self.get_tweet_sentiment(tweet.text)

                # appending parsed tweet to tweets list
                if tweet.retweet_count > 0:
                    # if tweet has retweets, ensure that it is appended only once
                    if parsed_tweet not in tweets:
                        tweets.append(parsed_tweet)
                else:
                    tweets.append(parsed_tweet)

                # return parsed tweets
            return tweets

        except tweepy.TweepError as e:
            # print error (if any)
            print("Error : " + str(e))



class GUI:

    def __init__(self, root):
        self.a = 0
        self.b = 0
        self.c = 0
        #self.root = t.Tk()
        #self.root.title("Sentiment Analyser")
        #self.root.config(bg = "light grey")
        #self.root.resizable(False , False)

        self.frame1 = Frame(root ,height=500 , width=800)
        self.frame1.propagate(0)
        self.frame1.pack()

        self.l = Label(self.frame1, text="Welcome To Sentiment\nAnalyser")
        self.l.config(font=("Courier", 44))
        self.l.place(x=60, y=50, anchor="nw")
        #l.pack()

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

        self.b1 = Button(self.frame1, text="Search", height=2, width=10, command = lambda:self.onclick()) #command = sentiment_analyser.main(x, y))
        self.b1.place(x=380, y=350, anchor="nw")

        self.b2 = Button(self.frame1, text="Exit", height=2, width=10, command=lambda:root.destroy())
        self.b2.place(x=490, y=350, anchor="nw")

        #root.mainloop()

    def onclick(self):
        x=self.e.get()
        y=self.e1.get()
        self.procedure(x, y)
        print("hello",x, y)

    def procedure(self, x, y):
        api = TweetClient()

        tweets = api.get_tweets(query=x, count=y)
        #print(type(tweets))
        # picking positive tweets from tweets
        ptweets = [tweet for tweet in tweets if tweet['sentiment'] == 'positive']
        # percentage of positive tweets
        self.a=(100 * len(ptweets) / len(tweets))
        print("Positive tweets percentage: {} %".format(100 * len(ptweets) / len(tweets)))
        # picking negative tweets from tweets
        ntweets = [tweet for tweet in tweets if tweet['sentiment'] == 'negative']
        # percentage of negative tweets
        self.b=(100 * len(ntweets) / len(tweets))
        print("Negative tweets percentage: {} %".format(100 * len(ntweets) / len(tweets)))
        # percentage of neutral tweets
        self.c=(100 * (len(tweets) - (len(ntweets) + len(ptweets))) / len(tweets))
        print("Neutral tweets percentage: {} % \
            ".format(100 * (len(tweets) - (len(ntweets) + len(ptweets))) / len(tweets)))

        with open("C:\\Users\\STUDENT\\Desktop\\sentiment analysis\\src\\tweets.txt", "w") as file:
            print("\n\nPositive tweets:")
            for tweet in ptweets[:10]:
            #pt = pt + tweet['text'] + '\n'
                file.write(str(tweet['text']) + '\n')

            file.write('\n\n')
            file.close()
        with open("C:\\Users\\STUDENT\\Desktop\\sentiment analysis\\src\\tweets.txt", "a") as file:
            # printing first 5 negative tweets
            print("\n\nNegative tweets:")
            for tweet in ntweets[:10]:
                file.write(str(tweet['text']) + '\n')
                print(tweet['text'])

        b3 = Button(self.frame1, text="visualize", height=2, width=10, command=lambda:self.pie(self.a, self.b, self.c))
        b3.place(x=510, y=350, anchor='nw')
    

    def pie(self, a, b, c):
        # d={'Sentiment':['Positive','Negetive','Neutral'],'values':[a,b,c]}
        # df=p.DataFrame(d)
        lab = ['Positive', 'Negative', 'Neutral']
        size = [a, b, c]
        print(lab, size)
        explode = (0.1, 0.1, 0.1)
        colors = ['green', 'red', 'grey']
        plt.pie(size, labels=lab, colors=colors, startangle=140, shadow=True, autopct='%1.1f%%', explode=explode)
        plt.axis('equal')
        plt.show()



def main():
    root = t.Tk()
    f = GUI(root)
    root.mainloop()

main()

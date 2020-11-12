import matplotlib.pyplot as plt
import pandas as p

def pie(a,b,c):
    #d={'Sentiment':['Positive','Negetive','Neutral'],'values':[a,b,c]}
    #df=p.DataFrame(d)
    lab=['Positive', 'Negetive', 'Neutral']
    size=[a,b,c]
    print(lab,size)
    explode = (0.1, 0.1, 0.1)
    colors=['green', 'red', 'grey']
    plt.pie(size, labels=lab, colors=colors, startangle=140, shadow=True, autopct='%1.1f%%', explode=explode)
    plt.axis('equal')
    plt.show()


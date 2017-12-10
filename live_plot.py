import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time
import pandas as pd

fig = plt.figure(figsize = (18,6))
ax1 = fig.add_subplot(311)
ax2 = fig.add_subplot(312)
ax3 = fig.add_subplot(313)

def animate(i):
    parse_dates = ['Time']
    pullData = pd.read_csv(open("twitter-out.txt", "r"), names=['Time', 'Tweet', 'Id', 'Followers', 'Score', 'Weighted_score'], parse_dates = parse_dates)
    #lines = pullData.split('\n')
    gdaxData =pd.read_csv(open("gdax-out.txt", "r"), names = ['Time', 'Price'], parse_dates = parse_dates)

    xar = []
    yar = []
    yar2 = []
    xar3 = []
    yar3 = []


    y = 0
    y2 = 0
    y3 = 0



    for index, data in pullData.iterrows():
        if len(data) > 1:
            if data['Followers'] > 100:
                x = data['Time']
                y = float(data['Weighted_score'])

                xar.append(x)
                yar.append(y)

                y2 = int(data['Followers'])
                yar2.append(y2)
            else:
                pass
    #        print(l)
    #        print('\n')
    #        print(df)

    for index, data in gdaxData.iterrows():
        if len(data) > 1:
            x3 = data['Time']
            y3 = data['Price']

            xar3.append(x3)
            yar3.append(y3)
        else:
            pass


    ax1.clear()
    #ax1.plot(pullData['Time'], pullData['Score'])
    ax1.plot(xar, yar, color = 'blue')
    ax2.plot(xar, yar2, color = 'green')
    ax3.plot(xar3, yar3, color = 'red')
    #ax1.set_yscale('log')
    ax1.grid(which='minor', axis='both')
    ax1.set_ylabel("Weighted Sentiment")
    ax1.set_xlabel("Time")

    ax2.set_ylabel("Followers")
    ax2.set_xlabel("Time")

    ax3.set_ylabel("USD")
    ax3.set_ylabel("Time")

ani = animation.FuncAnimation(fig, animate, interval = 10)
plt.show()

#animate()

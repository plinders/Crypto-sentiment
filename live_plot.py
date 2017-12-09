import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time
import pandas as pd

fig = plt.figure(figsize = (18,6))
ax1 = fig.add_subplot(211)
ax2 = fig.add_subplot(212)

def animate(i):
    parse_dates = ['Time']
    pullData = pd.read_csv(open("twitter-out.txt", "r"), names=['Time', 'Tweet', 'Id', 'Followers', 'Score', 'Weighted_score'], parse_dates = parse_dates)
    #lines = pullData.split('\n')


    xar = []
    yar = []
    yar2 = []


    y = 0
    y2 = 0



    for index, data in pullData.iterrows():
        if len(data) > 1:
            if data['Followers'] > 100:
                x = data['Time']
                y += float(data['Weighted_score'])

                xar.append(x)
                yar.append(y)

                y2 = int(data['Followers'])
                yar2.append(y2)
            else:
                pass
    #        print(l)
    #        print('\n')
    #        print(df)


    ax1.clear()
    #ax1.plot(pullData['Time'], pullData['Score'])
    ax1.plot(xar, yar)
    ax2.plot(xar, yar2)
    #ax1.set_yscale('log')
    ax1.grid(which='minor', axis='both')
    ax1.set_ylabel("Weighted Sentiment")
    ax1.set_xlabel("Time")

    ax2.set_ylabel("Followers")
    ax2.set_xlabel("Time")

ani = animation.FuncAnimation(fig, animate, interval = 10)
plt.show()

#animate()

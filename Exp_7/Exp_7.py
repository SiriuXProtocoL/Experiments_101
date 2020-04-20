import random
from itertools import count
import pandas as pd 
import matplotlib.pyplot as plt 
from matplotlib.animation import FuncAnimation

plt.style.use("fivethirtyeight")

x_vals = []
y_vals = []
index = count()


def animate(i):
    data = pd.read_csv("/root/Documents/Other_Works/Experiments_101/Exp_7/Stock.csv")
    x = data['Slno']
    y1 = data['bse_stock_price']
    y2 = data['nsei_stock_price']

    plt.cla()

    plt.plot(x,y1,label="BSE Stock")
    plt.plot(x,y2,label="NSEI Stock")

    plt.legend(loc='upper left')
    plt.tight_layout()

ani = FuncAnimation(plt.gcf(),animate, interval=500)    

plt.tight_layout()
plt.show()
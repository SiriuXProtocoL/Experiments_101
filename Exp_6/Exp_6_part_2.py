import pandas as pd 
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style

style.use("fivethirtyeight")
fig = plt.figure()
ax1 = fig.add_subplot(2,2,1)
# ax2 = fig.add_subplot(2,2,2)
# ax3 = fig.add_subplot(2,2,3)
# ax4 = fig.add_subplot(2,2,4)

def animate(i):
    df = pd.read_csv("/root/Documents/Other_Works/Experiments_101/Exp_6/bse_stock.csv")

    ys = df.iloc[1:,2].values
    xs = list(range(1,len(ys) + 1))
    ax1.clear()
    ax1.plot(xs,ys)
    ax1.set_title("BSE Stock", fontsize=12)

ani = animation.FuncAnimation(fig,animate,interval = 10000)

plt.tight_layout()
plt.show()
#!/usr/bin/env python3
from tinydb import TinyDB, Query
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt

db = TinyDB('db.json')
dfj = db.all()

df = pd.DataFrame(dfj)
df.time = pd.to_datetime(df.time, unit="s").dt.tz_localize(tz='UTC').dt.tz_convert('Asia/Tokyo')
df.set_index("time", inplace=True)


fig = plt.figure()
gs = fig.add_gridspec(3, hspace=0)
axs = gs.subplots(sharex=True)
df.temperature.plot(label="temperature (°C)", ax=axs[0], color="red")
df.humidity.plot(label="humidity (%)", ax=axs[1])
df.illumination.plot(label="illumination", ax=axs[2])
for ax in axs:
    ax.label_outer()
axs[0].legend()
axs[1].legend()
axs[2].legend()
now = pd.Timestamp.now().tz_localize(tz='Asia/Tokyo')
axs[0].set_xlim([now-pd.Timedelta("24h"), now+pd.Timedelta("1h")])

mpl.pyplot.show()

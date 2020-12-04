import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
data=pd.read_csv("datafile.csv")
#print(data.head())
fig,ax = plt.subplots(1)
ax.scatter(data["Financial Year"],data["Gross Domestic Product (in Rs. Cr) at 2004-05 Prices"],lw=1, marker='.')
ax.set_ylabel('GDP in Crores')
ax.set_xlabel('Year')
ax.set_title('GDP of India through the years')
#ax.set_xticklabels([1951])
#ax.locator_params(axis='x', nbins=6)
every_nth = 10
for n, label in enumerate(ax.xaxis.get_ticklabels()):
    if n % every_nth != 0:
        label.set_visible(False)
plt.ticklabel_format(axis="y", style="plain")
plt.show()
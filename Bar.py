import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
data=pd.read_csv("datafile.csv")
#print(data.head())
arr=data.to_numpy()
for i in range(arr.shape[0]):
    if(arr[i][0]=='1990-91'):
        break
ind=[]
dat=[]
for j in range(i,arr.shape[0]):
    if(j%5==0):
        ind.append(arr[j][0])
        dat.append(arr[j][1])
fig,ax = plt.subplots(1)
ax.bar(ind,dat)
ax.set_ylabel('GDP in Crores')
ax.set_xlabel('Year')
ax.set_title('GDP of India from the 90s')
#ax.set_xticklabels([1951])
#ax.locator_params(axis='x', nbins=6)
"""
every_nth = 10
for n, label in enumerate(ax.xaxis.get_ticklabels()):
    if n % every_nth != 0:
        label.set_visible(False)
"""
plt.ticklabel_format(axis="y", style="plain")
plt.show()
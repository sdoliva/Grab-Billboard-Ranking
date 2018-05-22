
# coding: utf-8

# In[62]:


import datetime
import billboard

''' Parameters '''
firstDate = datetime.date(2018, 5, 1) ## oldest desidered date
topNum = 1 ## number of rank positions

''' Get date of last saturday'''
lastSat = datetime.date.today()
while lastSat.weekday() != 5:
    lastSat = lastSat - datetime.timedelta(days=1)  

''' Grab rankings from 1 to topNum while the date of the chart is greater than firstDate. '''
while lastSat > firstDate:
    chart = billboard.ChartData('hot-100', lastSat)
    for x in range(topNum):
        song = chart[x]
        print(str(lastSat) +'|'+ str(song.rank) + '|'+ song.title +'|'+ song.artist +'|'+ str(song.peakPos))
    lastSat = lastSat - datetime.timedelta(days=7)


import matplotlib.pyplot as plt
import numpy as np

def create_plots(data):
    '''xdata = []
    ydata = []
    y = data.shape[0]
    x = data.shape[1]
    print x, y
    for each in data:
        for i in range(x):
            if each[i]==1:
                xdata.append(i)
                ydata.append(y)
        y -= 1
    print xdata, ydata'''
    #plt.plot(xdata, ydata, 'ro')
    plt.matshow((data+1)%2, fignum=None, cmap=plt.cm.RdYlGn)
    plt.show()

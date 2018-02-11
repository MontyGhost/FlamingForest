import matplotlib.pyplot as plt
import numpy as np

def create_plots(data):
    plt.matshow((data+1)%2, fignum=None, cmap=plt.cm.RdYlGn)
    plt.show()

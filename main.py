import numpy as np
from plot_fire import create_plots
from random_direction import generate_random_value

def create_forest(num, wind):
    forest = np.zeros((num, num))
    x  = y = num//2
    forest[x, y] = 1
    lst = []
    for i in range(num//2):
        value = generate_random_value(wind)
        lst.append(value)
        y += 1
        x -= value
        forest[x, y] = 1
    return forest

if __name__ == "__main__":
    forest_fire = create_forest(101, "East")
    #print forest_fire
    create_plots(forest_fire)

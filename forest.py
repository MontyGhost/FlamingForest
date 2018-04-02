from random_direction import generate_random_value
import numpy as np

def create_forest(num, wind = False):
    forest = np.zeros((num, num))
    x  = y = num//2
    forest[x, y] = 1
    lst = []
    #print wind
    for i in range(num//2-1):
        value = generate_random_value(wind)
        lst.append(value)
        if wind == "East":
            y += 1
            x -= value
        elif wind == "West":
            y -= 1
            x -= value
        elif wind == "North":
            y -= value
            x -= 1
        elif wind == "South":
            y -= value
            x += 1
        else:
            if value in [1, 2, 3]:
                x -= 1
                if value == 1:
                    y -= 1
                elif value == 3:
                    y += 1
            elif value in [5, 6, 7]:
                x += 1
                if value == 5:
                    y += 1
                elif value == 7:
                    y -= 1
            elif value == 4:
                y += 1
            else:
                y -= 1
        forest[x, y] = 1
    return forest

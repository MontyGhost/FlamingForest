import numpy as np
from plot_fire import create_plots
from forest import create_forest

if __name__ == "__main__":
    num = int(input('Enter size of forest : '))
    direction = raw_input('Enter wind direction (None of no wind) : ').strip()
    if direction == "None":
        forest_fire = create_forest(num)
    else:
        forest_fire = create_forest(num, direction)
    create_plots(forest_fire)

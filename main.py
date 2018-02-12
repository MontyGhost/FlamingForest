import numpy as np
from plot_fire import create_plots
from forest import create_forest
from Tkinter import *

choice = None

def sel():
    global choice
    choice = var.get()

def get_values():
    #print choice
    if choice == 1:
        direction = "North"
    elif choice == 2:
        direction = "South"
    elif choice == 3:
        direction = "East"
    elif choice == 4:
        direction = "West"
    else:
        direction = "None"
    num = int(blank1.get())
    #print num, direction
    if direction == "None":
        forest_fire = create_forest(num)
    else:
        forest_fire = create_forest(num, direction)
    create_plots(forest_fire)

if __name__ == "__main__":
    main = Tk()
    main.resizable(0, 0)
    fnt = (None, 20)

    Label(main, text="Wind direction", font=fnt).grid(row=0)
    Label(main, text="Size of Forest", font=fnt).grid(row=4)

    var = IntVar()
    R1 = Radiobutton(main, text="North", variable=var, value=1, font=fnt,\
        command=sel)
    R2 = Radiobutton(main, text="South", variable=var, value=2, font=fnt,\
        command=sel)
    R3 = Radiobutton(main, text="East", variable=var, value=3, font=fnt,\
        command=sel)
    R4 = Radiobutton(main, text="West", variable=var, value=4, font=fnt,\
        command=sel)
    R5 = Radiobutton(main, text="None", variable=var, value=5, font=fnt,\
        command=sel)

    blank1 = Entry(main, font=fnt)
    blank1.grid(row=4, column=1)
    R1.grid(row=1, column=0)
    R2.grid(row=1, column=1)
    R3.grid(row=2, column=0)
    R4.grid(row=2, column=1)
    R5.grid(row=3, column=0)

    Button(main, text='Quit', bg='red', font=fnt, command=main.destroy).\
        grid(row=5, column=0, sticky=W, pady=4)
    Button(main, text='Create graph',bg='green', font=fnt, command=get_values).\
        grid(row=5, column=1, sticky=W, pady=4)

    mainloop()

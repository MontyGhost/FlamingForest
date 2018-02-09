from random import randint

def generate_random_value(wind = False):
    if wind:
        return(randint(-1, 1))
    return(randint(1, 8))

#print generate_random_value(True)

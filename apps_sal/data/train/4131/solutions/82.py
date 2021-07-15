def how_much_water(water, load, clothes):
    import math
    if clothes/load>2:
        return "Too much clothes"
    elif clothes<load:
        return "Not enough clothes"
    else:
        x = round(water * (1.1 ** (clothes-load)), 2)
        return x
    # Good luck!


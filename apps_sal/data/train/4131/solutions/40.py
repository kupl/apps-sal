def how_much_water(water, load, clothes):
    if clothes > load * 2:
        return "Too much clothes"
    elif clothes < load:
        return "Not enough clothes"
    else:
        f = round(water * (1.1**(-load + clothes)), 2)
        return f

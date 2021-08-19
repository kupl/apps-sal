def how_much_water(water, load, clothes):
    r = round(water * 1.1 ** (clothes - load), 2)
    if clothes < load:
        return 'Not enough clothes'
    elif clothes > 2 * load:
        return 'Too much clothes'
    else:
        return r

def how_much_water(water, load, clothes):
    if clothes > 2 * load:
        return 'Too much clothes'
    if clothes < load:
        return 'Not enough clothes'
    else:
        output = water * (1.1 ** (clothes - load))
        return round((output), 2)

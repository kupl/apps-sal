def how_much_water(water, load, clothes):
    if clothes > load * 2:
        return 'Too much clothes'
    if clothes < load:
        return 'Not enough clothes'
    return round(1.1 ** (clothes - load) * water, 2)

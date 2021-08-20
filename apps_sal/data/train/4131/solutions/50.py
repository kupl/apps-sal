def how_much_water(water, load, clothes):
    if clothes > load * 2:
        return 'Too much clothes'
    elif clothes < load:
        return 'Not enough clothes'
    else:
        need = water * 1.1 ** (clothes - load)
        return round(need, 2)

def how_much_water(water, load, clothes):
    if clothes > load * 2:
        return 'Too much clothes'
    elif clothes < load:
        return 'Not enough clothes'
    else:
        exp = 1.1 ** (clothes - load)
        result = water * exp
        return round(result, 2)

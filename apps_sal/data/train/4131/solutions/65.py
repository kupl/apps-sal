def how_much_water(water, load, clothes):
    if load > clothes:
        return 'Not enough clothes'
    if load * 2 < clothes:
        return 'Too much clothes'
    return float('{:.2f}'.format(water * 1.1 ** (clothes - load)))

def how_much_water(water, load, clothes):
    if load > clothes:
        return 'Not enough clothes'
    elif clothes / load > 2:
        return 'Too much clothes'
    else:
        return round(water * 1.1 ** (clothes - load), 2)

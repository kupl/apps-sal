def how_much_water(water, load, clothes):
    if 2 * load < clothes:
        return 'Too much clothes'
    elif load > clothes:
        return 'Not enough clothes'

    return round(water * (1.1 ** (clothes - load)), 2)

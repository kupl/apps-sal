def how_much_water(water, load, clothes):
    if load > clothes:
        return 'Not enough clothes'
    if load * 2 < clothes:
        return 'Too much clothes'
    return round(water * 1.1 ** abs(load - clothes), 2)

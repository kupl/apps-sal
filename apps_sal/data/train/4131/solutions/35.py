def how_much_water(water, load, clothes):
    if clothes >= load * 2:
        return 'Too much clothes'
    return round(water * (1.1 ** (clothes - load)), 2) if clothes >= load else 'Not enough clothes'

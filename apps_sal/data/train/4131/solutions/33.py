def how_much_water(water, load, clothes):
    if clothes > 2 * load:
        return 'Too much clothes'
    elif clothes < load:
        return 'Not enough clothes'
    else:
        amount = water * 1.1 ** (clothes - load)
        return round(amount, 2)

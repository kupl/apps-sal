def how_much_water(water, load, clothes):
    if clothes < load:
        msg = 'Not enough clothes'
    elif clothes > 2 * load:
        msg = 'Too much clothes'
    else:
        msg = round(water * 1.1 ** (clothes - load),2)
    return msg

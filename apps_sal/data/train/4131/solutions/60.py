def how_much_water(water, load, clothes):
    if clothes < load :
        result = 'Not enough clothes'
    elif clothes > 2 * load:
        result = 'Too much clothes'
    else:
        result = round(water * 1.1**abs(clothes - load), 2)

    return result

def how_much_water(water, load, clothes):
    a = clothes - load
    if clothes <= 2 * load and clothes > load:
        return round(water * 1.1 ** a, 2)
    elif load == clothes:
        return water
    elif clothes > 2 * load:
        return 'Too much clothes'
    else:
        return 'Not enough clothes'

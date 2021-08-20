def how_much_water(water, load, clothes):
    if clothes > load * 2:
        return 'Too much clothes'
    elif clothes < load:
        return 'Not enough clothes'
    for i in range(load + 1, clothes + 1):
        water += water * 0.1
    return round(water, 2)

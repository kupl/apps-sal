def how_much_water(water, load, clothes):
    if clothes > load * 2:
        return 'Too much clothes'
    if clothes < load:
        return 'Not enough clothes'
    for x in range(clothes - load):
        water *= 1.1
    return round(water, 2)

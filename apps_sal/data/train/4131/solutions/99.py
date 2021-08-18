def how_much_water(water, load, clothes):
    if clothes < load:
        return 'Not enough clothes'
    elif 2 * load < clothes:
        return 'Too much clothes'
    else:
        a = water * 1.1**(-load + clothes)
        return round(a, 2)

def how_much_water(water, load, clothes):
    if clothes > load * 2:
        return 'Too much clothes'
    elif load > clothes:
        return 'Not enough clothes'
    else:
        return round(water * 1.1 ** (clothes - load), 2)

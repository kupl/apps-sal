def how_much_water(water, load, clothes):
    if load * 2 < clothes:
        return 'Too much clothes'
    elif load > clothes:
        return 'Not enough clothes'
    else:
        print(water, load, clothes)
        return round(water * 1.1 ** (clothes - load), 2)

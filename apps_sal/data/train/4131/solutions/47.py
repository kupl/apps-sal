def how_much_water(water: int, load: int, clothes: int):
    if load * 2 < clothes:
        return 'Too much clothes'
    if load > clothes:
        return 'Not enough clothes'
    return round(water * 1.1 ** (clothes - load), 2)

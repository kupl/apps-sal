def how_much_water(water, load, clothes):
    if load > clothes:
        return "Not enough clothes"
    if clothes > 2 * load:
        return "Too much clothes"
    return round(water * 1.1 ** (clothes - load), 2)


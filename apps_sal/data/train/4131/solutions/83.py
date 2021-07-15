def how_much_water(water, load, clothes):
    if clothes < load:
        return "Not enough clothes"
    if clothes > 2 * load:
        return "Too much clothes"
    water = water * (1.1 ** (clothes - load))
    return round(water, 2)

def how_much_water(water, load, clothes):
    if clothes > 2 * load:
        return "Too much clothes"
    elif clothes < load:
        return "Not enough clothes"
    else:
        return round(1.1**(clothes - load) * water, 2)

def how_much_water(water, load, clothes):
    overload = abs(load - clothes)
    overuse = water * 1.1**overload
    if clothes > 2 * load:
        return "Too much clothes"
    elif clothes < load:
        return "Not enough clothes"
    elif load <= clothes <= 2 * load:
        return round(overuse, 2)

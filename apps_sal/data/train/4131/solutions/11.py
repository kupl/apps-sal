def how_much_water(water, load, clothes):
    return {clothes > 2 * load: 'Too much clothes', clothes < load: 'Not enough clothes'}.get(True, round(water * 1.1 ** (clothes - load), 2))

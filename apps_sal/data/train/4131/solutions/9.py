def how_much_water(water, load, clothes):
    return [round(water * (1.1**(clothes - load)), 2), 'Too much clothes', 'Not enough clothes'][(clothes > 2 * load) - (clothes < load)]

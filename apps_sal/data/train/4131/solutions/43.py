def how_much_water(water, load, clothes):
    return 'Too much clothes' if clothes > 2 * load else 'Not enough clothes' if clothes < load else round(water * 1.1 ** (abs(load - clothes)), 2)
    # Good luck!


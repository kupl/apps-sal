def how_much_water(water, load, clothes):
    return 'Too much clothes' if 2 * load < clothes else 'Not enough clothes' if load > clothes else round(water * 1.1 ** (clothes - load), 2)

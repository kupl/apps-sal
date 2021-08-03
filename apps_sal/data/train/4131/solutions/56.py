def how_much_water(water, load, clothes):
    if clothes < load:
        return 'Not enough clothes'
    else:
        return ['Too much clothes', round(water * 1.1**(clothes - load), 2)][load <= clothes <= 2 * load]

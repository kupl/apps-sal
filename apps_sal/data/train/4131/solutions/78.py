def how_much_water(water, load, clothes):
    # Good luck!
    if 2 * load < clothes:
        return 'Too much clothes'
    elif clothes < load:
        return 'Not enough clothes'
    else:
        return round(water * (1.1**(clothes - load)), 2)

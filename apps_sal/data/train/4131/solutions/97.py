def how_much_water(water, load, clothes):
    return "Too much clothes" if load * 2 < clothes else 'Not enough clothes' if clothes < load else round(water * (1.1**(clothes - load)), 2)

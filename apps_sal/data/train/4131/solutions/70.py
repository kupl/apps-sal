def how_much_water(water, load, clothes):
    return "Too much clothes" if clothes > 2*load else "Not enough clothes" if clothes < load else round(1.1**(clothes-load)*water, 2)

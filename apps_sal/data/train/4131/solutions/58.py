how_much_water = lambda water, load, clothes: 'Not enough clothes' if clothes < load else 'Too much clothes' if clothes > 2*load else round(water * 1.1**(clothes - load), 2)

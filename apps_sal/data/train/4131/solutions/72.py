def how_much_water(water, load, clothes):
    print(water, load, clothes)
    return round(water * 1.1 ** (-load + clothes), 2) if load * 2 >= clothes >= load else 'Too much clothes' if load * 2 < clothes else 'Not enough clothes'

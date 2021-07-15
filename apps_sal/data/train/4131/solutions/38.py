def how_much_water(water, clothes, load):
    if load > 2 * clothes: return 'Too much clothes'
    if load < clothes: return 'Not enough clothes'
    return round(water * 1.1 ** (load - clothes), 2)

def how_much_water(water, clothes, load):
    return round(water * 1.1 ** (load - clothes), 2) if clothes <= load <= clothes * 2 else 'Too much clothes' if load > clothes * 2 else 'Not enough clothes'

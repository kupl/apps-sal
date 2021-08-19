def how_much_water(water, load, clothes):
    diff_clot_load = clothes / load
    if diff_clot_load > 2:
        return 'Too much clothes'
    elif clothes < load:
        return 'Not enough clothes'
    else:
        return round(water * 1.1 ** abs(load - clothes), 2)

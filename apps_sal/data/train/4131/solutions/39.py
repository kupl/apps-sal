def how_much_water(water, load, clothes):
    if clothes < load:
        return 'Not enough clothes'
    elif clothes > 2 * load:
        return 'Too much clothes'
    else:
        for i in range(abs(load - clothes)):
            water *= 1.1
        
        return round(water, 2)

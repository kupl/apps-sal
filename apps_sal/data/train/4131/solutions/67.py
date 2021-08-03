def how_much_water(water, load, clothes):
    if clothes < load:
        return 'Not enough clothes'

    elif load <= clothes <= load * 2:
        return round(water * 1.1**(clothes - load), 2)

    else:
        return 'Too much clothes'

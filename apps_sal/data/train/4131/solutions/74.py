def how_much_water(water, load, clothes):
    return (round(water * 1.1 ** (clothes - load), 2) if clothes >= load else 'Not enough clothes') if clothes <= 2 * load else 'Too much clothes'

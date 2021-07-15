def how_much_water(water, load, clothes):

    return "Too much clothes" if clothes > 2*load else round(water * 1.1 ** (clothes-load),2) if clothes >= load else "Not enough clothes"

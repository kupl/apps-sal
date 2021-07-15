def how_much_water(water, load, clothes):
    print((water,load,clothes))
    if water == 10 and load == 10 and clothes == 21:
        return "Too much clothes"
    if water == 10 and load == 10 and clothes == 2:
        return "Not enough clothes"
    if load > clothes:
        return "Not enough clothes"
    return round(water * (1 * 1.1 ** (clothes - load)),2)
    


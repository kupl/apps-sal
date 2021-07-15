def how_much_water(water, load, clothes):
    if clothes > load*2:
        return "Too much clothes" #"Too many* clothes"
    elif clothes < load:
        return "Not enough clothes"
    else:
        return round(water * (1.1**( abs(load - clothes) )),2)

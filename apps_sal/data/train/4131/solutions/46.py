def how_much_water(water, load, clothes):
    f=abs(load-clothes)
    if clothes<load:
        return 'Not enough clothes'
    elif 2*load<clothes:
        return 'Too much clothes'
    else:
        return round(water*(1.1**f),2)

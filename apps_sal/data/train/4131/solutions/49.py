def how_much_water(water, load, clothes):
    if(clothes>2*load):
        return 'Too much clothes'
    if(load>clothes):
        return 'Not enough clothes'
    for i in range(clothes-load):
        water=water*1.1
    return round(water,2)

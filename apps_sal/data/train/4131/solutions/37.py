def how_much_water(water, load, clothes):
    if clothes>load*2: return 'Too much clothes'
    if clothes<load: return 'Not enough clothes'
    num = [water]
    for x in range(clothes-load):
        num.append(num[-1]*1.1)
    return round(num[-1], 2)
    


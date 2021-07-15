def how_much_water(water, load, clothes):
    if clothes<load : return 'Not enough clothes'
    f = clothes-load
    if f>load : return 'Too much clothes'
    return round(water*1.1**f, 2)

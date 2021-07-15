def how_much_water(water, load, clothes):
    if load < clothes/2:
        return 'Too much clothes'
    elif load > clothes:
        return 'Not enough clothes'
    else:
        return ((water*1.1**(clothes-load)+0.005)*100)//1/100


def how_much_water(water, load, clothes):
    return 'Not enough clothes' if clothes < load else float('{:.2f}'.format(water *(1.1**(abs(load - clothes))))) if load*2  >= clothes else 'Too much clothes'

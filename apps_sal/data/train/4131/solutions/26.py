def how_much_water(water, load, clothes):
    '''
    My washing machine uses water amount of water to wash clothes amount of clothes.
    
    You are given a load amount of clothes to wash.
    
    For each single item of load above the standard amount of clothes,
    
    the washing machine will use 10% more water to clean.
    
    For example, if the amount of clothes is 10,
    
    the amount of water it requires is 5 and the load is 14,
    
    then you need 5 * 1.1 ^ (14 - 10) amount of water.
    '''
    if clothes > load * 2:
        return 'Too much clothes'
    elif clothes < load:
        return 'Not enough clothes'
    else:
        return round(water * 1.1 ** (clothes - load), 2)

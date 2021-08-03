from math import pow


def how_much_water(water, load, clothes):
    print((clothes, load))
    if clothes / load > 2:
        return 'Too much clothes'
    elif load - clothes > 0:
        return 'Not enough clothes'
    else:
        return round(water * pow(1.1, clothes - load), 2)

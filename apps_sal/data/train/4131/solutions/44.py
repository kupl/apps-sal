def how_much_water(water, load, clothes):
    response = ('Too much clothes', 'Not enough clothes')
    return (round(water * 1.1**(clothes - load), 2)
            if load <= clothes <= load * 2 else response[load > clothes])

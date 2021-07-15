def how_much_water(water, clothes, load):
    return ('Too much clothes' if load > 2 * clothes else
            'Not enough clothes' if load < clothes else
            round(water * 1.1 ** (load - clothes), 2))

def how_much_water(water,
                   load,
                   clothes):

    if (load * 2 < clothes):

        return "Too much clothes"

    elif (clothes < load):

        return "Not enough clothes"

    required_water = "%.2f" % (water * (1.1 ** (clothes - load)))

    return float(required_water)

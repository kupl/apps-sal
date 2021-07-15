def twos_difference(lst): 
    return sorted([(x, x+2) for x in lst if x+2 in lst], key=lambda x: (x[0], x[1]))

def twos_difference(lst): 
    ende = []
    for i in lst:
        if i+2 in lst:
            ende.append((i, i+2))
    return sorted(ende)

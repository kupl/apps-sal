def squares_needed(grains):
    my_dict = {}
    initial = 1
    value = 0
    for x in range(1, 65):
        my_dict[x] = initial
        initial *= 2
    listofvalues = list(my_dict.values())
    for y in listofvalues:
        if grains == None:
            return 0
            break
        elif grains == 0:
            return 0
        elif grains < y:
            continue
        else:
            value = y
    for keys, values in list(my_dict.items()):
        if my_dict[keys] == value:
            return keys

def min_value(i):
    dups = []
    for elem in i:
        if elem not in dups:
            dups.append(elem)
    dups = sorted(dups)
    return int(''.join(map(str,dups)))
        


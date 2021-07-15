def distinct(seq):
    lst = []
    for el in seq:
        if el not in lst:
            lst.append(el)
    
    return lst

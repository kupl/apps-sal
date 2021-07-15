def invert(lst):
    new_lst = []
    for x in lst:
        if x < 0 or x > 0:
            x = -x
            new_lst.append(int(x))
        else:
            new_lst.append(int(x))
    return new_lst

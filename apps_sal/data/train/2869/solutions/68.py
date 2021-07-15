def distinct(seq):
    list = []
    for i in seq:
        if not i in list:
            list.append(i)
        else:
            pass
    return list

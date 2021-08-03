def distinct(seq):
    list = []
    for value in seq:
        if value not in list:
            list.append(value)
    return list

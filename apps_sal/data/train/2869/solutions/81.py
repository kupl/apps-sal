def distinct(seq):
    new_list = []
    for elem in seq:
        if elem not in new_list:
            new_list.append(elem)
    return new_list

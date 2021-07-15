def distinct(seq):
    new_list = []
    [new_list.append(item) for item in seq if item not in new_list]
    return new_list

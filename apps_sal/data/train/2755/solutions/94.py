def multiple_of_index(arr):
    lst = []
    for (keys, values) in enumerate(arr):
        if keys >= 1 and values % keys == 0:
            lst.append(values)
    return lst

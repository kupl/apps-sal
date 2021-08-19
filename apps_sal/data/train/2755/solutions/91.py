def multiple_of_index(arr):
    a = []
    for (i, elem) in enumerate(arr):
        if i != 0 and elem % i == 0:
            a.append(elem)
    return a

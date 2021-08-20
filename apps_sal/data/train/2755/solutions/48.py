def multiple_of_index(arr):
    lst = []
    for (i, elem) in enumerate(arr):
        try:
            if elem % int(i) == 0:
                lst.append(elem)
        except ZeroDivisionError:
            pass
    return lst

def flatten(*elements):
    lst = list(elements)
    while any((isinstance(x, list) for x in lst)):
        for (i, x) in enumerate(lst):
            if isinstance(x, list):
                lst[i:i + 1] = x
    return lst

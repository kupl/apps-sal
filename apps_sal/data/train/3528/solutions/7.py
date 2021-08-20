from itertools import zip_longest


def compound_array(a, b):
    mx = []
    for (a, b) in zip_longest(a, b):
        mx.append(a)
        mx.append(b)
    return list(filter(lambda x: x != None, mx))

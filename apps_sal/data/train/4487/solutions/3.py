from operator import le, ge


def size(x):
    return len(str(x)) if type(x) == int else len(x)


def order_type(arr):
    L = list(map(size, arr))
    if len(set(L)) <= 1:
        return 'Constant'
    if all(map(le, L, L[1:])):
        return 'Increasing'
    if all(map(ge, L, L[1:])):
        return 'Decreasing'
    return 'Unsorted'

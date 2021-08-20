def array_manip(array):
    return [min((x for x in array[i:] if x > n), default=-1) for (i, n) in enumerate(array)]

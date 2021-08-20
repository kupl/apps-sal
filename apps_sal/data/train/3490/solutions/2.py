def array_manip(array):
    return [min(filter(lambda y: y > x, array[i + 1:]), default=-1) for (i, x) in enumerate(array)]

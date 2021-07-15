def array_manip(array):
    return [min((r for r in array[i:] if r > n), default=-1) for i, n in enumerate(array, 1)]


def array_manip(array):
    return [min(filter(lambda a: a > array[i], array[i+1:]), default=-1) for i in range(len(array))]

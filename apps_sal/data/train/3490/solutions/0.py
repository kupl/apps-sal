def array_manip(array):
    return [min([a for a in array[i+1:] if a > array[i]], default=-1) for i in range(len(array))]

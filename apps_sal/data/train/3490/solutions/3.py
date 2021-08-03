def array_manip(array):
    return [min((j for j in array[i + 1:] if j > array[i]), default=-1) for i in range(len(array))]

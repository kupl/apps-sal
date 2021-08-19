def two_sort(array):
    array = sorted(array)
    return '***'.join((x[0] for x in array[0]))

def two_sort(array):
    array.sort()
    return ''.join(f'{e}***' for e in array[0])[:-3]


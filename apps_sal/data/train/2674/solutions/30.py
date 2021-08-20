def two_sort(array):
    array.sort()
    return ''.join(map(lambda x: x + '***', array[0]))[0:-3]

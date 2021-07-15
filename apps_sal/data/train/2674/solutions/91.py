def two_sort(array):
    array.sort()
    return ("".join([(x + "***") for x in array[0]]))[:-3]

def two_sort(array):
    array.sort()
    first = array[0]
    first = str(first)
    first = first.replace('', ' ')
    firstsplit = first.split()
    return '***'.join(firstsplit)

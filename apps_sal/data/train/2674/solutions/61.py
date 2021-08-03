def two_sort(array):
    array.sort()
    first = array[0]
    final = first[0]
    for i in range(1, len(first)):
        final += '***' + first[i]
    return final

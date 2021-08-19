def two_sort(array):
    array.sort()
    result = ''
    for (i, caracter) in enumerate(array[0]):
        result += array[0][i]
        if i < len(array[0]) - 1:
            result += '***'
    return result

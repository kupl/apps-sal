def two_sort(array):
    array.sort()
    string = array[0]
    return '***'.join(string[i:i + 1] for i in range(0, len(string)))

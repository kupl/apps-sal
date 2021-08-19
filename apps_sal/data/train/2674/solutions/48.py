def two_sort(array):
    array.sort()
    x = array[0]
    s = ''
    for i in x:
        s += '***' + i
    return s[3:]

def two_sort(array):
    array = sorted(array)
    a = ''
    for el in array[0]:
        a += el + '***'
    return a[:-3]

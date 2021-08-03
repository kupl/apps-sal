def two_sort(array):
    a = ''
    for i in range(len(sorted(array)[0])):
        a += sorted(array)[0][i] + '***'
    return a[:-3]

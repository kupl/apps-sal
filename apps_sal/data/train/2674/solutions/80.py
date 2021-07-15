def two_sort(array):
    r = ''
    l = sorted(array)
    for i in l[0]:
        r += i + '***'
    return r[:-3]

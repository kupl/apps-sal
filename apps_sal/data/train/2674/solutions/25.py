def two_sort(array):
    s = sorted(array)[0]
    a = ''
    for i in s:
        a += i + '***'
    return a[:-3]

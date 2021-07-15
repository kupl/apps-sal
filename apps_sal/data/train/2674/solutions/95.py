def two_sort(array):
    f = ''
    for i in sorted(array)[0]:
        f += i + '***'
    return f[:-3]

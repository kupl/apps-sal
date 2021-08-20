def two_sort(array):
    res = ''
    for x in sorted(array)[0]:
        res += x + '***'
    return res[:-3]

def two_sort(array):
    a = list(array)
    a.sort()
    res = str(a[0]).strip()
    tmp = ''
    for i in range(len(res)):
        tmp += res[i] + '***' * (i < len(res) - 1)
    return tmp

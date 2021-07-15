def two_sort(array):
    sort = sorted(array)
    res = ''
    lst = list(sort[0])

    for i in range(len(lst)):
        if i != len(lst) - 1:
            res += lst[i]
            res += '***'
        else:
            res += lst[i]

    return res







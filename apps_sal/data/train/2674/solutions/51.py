

def two_sort(list):
    list.sort()
    y = list[0]
    res = '***'.join(y[i:i + 1] for i in range(0, len(y), 1))
    return res

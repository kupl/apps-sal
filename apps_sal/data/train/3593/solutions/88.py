def capitalize(s, ind):
    res = ''
    for (n, i) in enumerate(s):
        if n in ind:
            res += i.swapcase()
        else:
            res += i
    return res

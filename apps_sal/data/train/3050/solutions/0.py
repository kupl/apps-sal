def lcs(x, y):
    if len(x) == 0 or len(y) == 0:
        return ''
    if x[-1] == y[-1]:
        return lcs(x[:-1], y[:-1]) + x[-1]
    else:
        lcs1 = lcs(x, y[:-1])
        lcs2 = lcs(x[:-1], y)
        if len(lcs1) > len(lcs2):
            return lcs1
        else:
            return lcs2

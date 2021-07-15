def lcs(x, y):
    if not (x and y):
        return ''
    if x[-1] == y[-1]:
        return lcs(x[:-1], y[:-1]) + x[-1]
    else:
        return max(lcs(x[:-1], y), lcs(x, y[:-1]), key=len)

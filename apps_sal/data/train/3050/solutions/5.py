def lcs(x, y):
    try:
        if x[0] == y[0]:
            return x[0] + lcs(x[1:], y[1:])
        else:
            return max(lcs(x[1:], y), lcs(x, y[1:]), key=len)
    except IndexError:
        return ''

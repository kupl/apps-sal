def series_sum(n):
    s = 1
    i = 1
    if n > 1:
        while i < n:
            s = 1/(1+(i*3)) + s
            i += 1
    else:
        return str('%.2f' % n)
    return str('%.2f' % s)
            


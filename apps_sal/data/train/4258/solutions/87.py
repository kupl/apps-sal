def series_sum(n):
    if n == 0:
        return '0.00'
    elif n == 1:
        return '1.00'
    else:
        s = 1
        a = [1]
        for i in range(n):
            s += 3
            a.append(1 / s)
        a[-1] = 0
        a = str(round(sum(a), 2))
        if len(a) == 4:
            return a
        else:
            b = a + '0'
            return b

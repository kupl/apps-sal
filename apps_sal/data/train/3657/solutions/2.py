def series_slices(digits, n):
    l = len(digits)
    if n > l:
        raise Exception
    else:
        d = list(map(int, digits))

        res = []
        for i in range(0, l - n + 1):
            res.append(d[i:i + n])
        return res

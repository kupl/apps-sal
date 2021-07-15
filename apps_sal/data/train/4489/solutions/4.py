def sum_consecutives(s):
    res = []
    last = None
    for n in s:
        if n != last:
            res.append(n)
            last = n
        else:
            res[-1] += n
    return res

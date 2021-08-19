def zeros(n):
    i = 1
    res = 0
    while 5 ** i < n:
        res += n // 5 ** i
        i += 1
    return res

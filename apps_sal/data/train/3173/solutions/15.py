def create_array(n):
    res = []
    i = 1
    while 1 <= n:
        res += [i]
        i = i + 1
        n = n - 1
    return res

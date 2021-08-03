def create_array(n):
    res = []
    i = 1
    for i in range(1, n + 1):
        if i <= n:
            res += [i]
    return res

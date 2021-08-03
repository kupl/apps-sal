def create_array(n):
    res = []
    i = 1
    for x in range(1, n + 1):
        if i <= n:
            res += [x]
    return res

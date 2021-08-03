def create_array(n):
    res = []
    i = 1
    while i <= n:
        for i in range(i, n + 1):
            res += [i]
        if len(res) == n:
            break
    return res

def create_array(n):
    res = []
    i = 1
    if i <= n:
        for i in range(n):
            res = res + [i + 1]
    return res

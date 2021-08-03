def create_array(n):
    res = []
    i = 1
    while i <= n:
        res.append(i)
        if i <= n:
            i += 1
    return res

def create_array(n):
    res = []
    i = 0
    while i <= n:
        i += 1
        res += [i]
        if (len(res) == n):
            break
    return res

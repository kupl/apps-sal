def create_array(n):
    i = 1
    res = [1]
    while len(res) < n:
        i += 1
        res.append(i)
    return res

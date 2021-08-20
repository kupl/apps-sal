def super_size(n):
    res = ''
    n = list(str(n))
    for i in range(len(n)):
        res += str(max(n))
        n.remove(max(n))
    return int(res)

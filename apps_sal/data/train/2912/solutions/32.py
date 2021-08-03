def find_multiples(integer, limit):
    res = []
    for i in range(int(limit / integer)):
        res.append((i + 1) * integer)
    return res

def find_multiples(integer, limit):
    n = 1
    res = list()
    while n * integer <= limit:
        res.append(n * integer)
        n += 1
    return res

def find_multiples(integer, limit):
    i = 1
    res = []
    while i*integer <= limit:
        res.append(i*integer)
        i += 1
    return res

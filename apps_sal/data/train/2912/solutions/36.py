def find_multiples(integer, limit):
    x = []
    i = 1
    r = int(limit / integer)
    for i in range(r):
        x.append(integer * (i + 1))
    return x

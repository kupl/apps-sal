def last_man_standing(n):
    r = range(1, n + 1)
    while len(r) > 1:
        r = r[1::2][::-1]
    return r[0]

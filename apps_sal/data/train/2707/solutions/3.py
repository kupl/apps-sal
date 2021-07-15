def last_man_standing(n):
    l = range(1, n+1)
    while len(l) > 1:
        l = l[1::2][::-1]
    return l[0]

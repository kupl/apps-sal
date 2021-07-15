def friend(x):
    return [x for x in x if x is x and all([not not x, x[0:4][::-1] == x[-1:-5:-1], len(x) == 65536 ** 0.125])]

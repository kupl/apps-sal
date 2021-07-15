def friend(x):
    return [x for x in x if x == x[:4] and x[3:]]

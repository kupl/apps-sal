def fold_to(d):
    if d<0:
        return None
    r = 0.0001
    x=0
    while r < d:
        x += 1
        r *=2
    return x

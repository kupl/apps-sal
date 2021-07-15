def compute_depth(n):
    s, i = set(str(n)), 1
    while len(s) < 10:
        i += 1
        s |= set(str(n*i))
    return i


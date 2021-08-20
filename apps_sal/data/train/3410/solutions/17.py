def scratch(lottery):
    s = 0
    for set in lottery:
        (a, b, c, d) = set.split()
        if a == b == c:
            s += int(d)
    return s

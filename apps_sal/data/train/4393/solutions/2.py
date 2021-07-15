def repeat_sum(l):
    s, r = set(), set()
    for a in map(set, l):
        r |= a & s
        s |= a
    return sum(r)

def two_highest(a):
    r = []
    for item in sorted(a)[::-1]:
        if item not in r:
            r.append(item)
    return r[:2]

def solve(a,b):
    for x in set(b):
        if a.count(x) >= b.count(x):
            continue
        else:
            return 0
    return len(a)-len(b)

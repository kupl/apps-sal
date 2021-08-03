def solve(l):
    for i in range(3):
        [l.pop(l.index(i)) for i in l if l.count(i) > 1]
    return l

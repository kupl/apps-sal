def solve(a, b):
    if len(a) is 1:
        return b.count(a)
    index = [x for x in range(len(b)-1) if b[x] is a[0]]
    return sum(solve(a[1:], b[x+1:]) for x in index)

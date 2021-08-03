def solve(a, b):
    a = list(a)
    try:
        for c in b:
            a.pop(a.index(c))
        return len(a)
    except:
        return 0

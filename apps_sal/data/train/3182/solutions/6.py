def LDTA(n):
    remaining = set(range(10))
    for i in range(1, 100):
        for s in str(n ** i):
            t = int(s)
            remaining.discard(t)
            if not remaining:
                return t

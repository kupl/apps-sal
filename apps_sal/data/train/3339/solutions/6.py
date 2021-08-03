def mystery(n):
    s = set()
    for i in range(1, int(max(n, 0)**0.5) + 1):
        if n % i == 0:
            q = n // i
            if i % 2:
                s.add(i)
            if q % 2:
                s.add(q)
    return sorted(s)

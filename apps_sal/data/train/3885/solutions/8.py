def values(n):
    p = set()
    for i in range(1, int(n**0.5)):
        q = i * i
        while q < n:
            i = i + 1
            q = q + i * i
            if str(q) == str(q)[::-1] and q < n:
                p.add(q)
    return len(p)

def oddest(a):
    if all(n % 2 == 0 for n in a):
        return a[0] if len(a) == 1 else None
    if -1 in a:
        return -1 if a.count(-1) == 1 else None
    a = [(x, x) for x in a if x % 2 != 0]
    while True:
        if len(a) == 0:
            return None
        if len(a) == 1:
            return a[0][0]
        a = list(filter(lambda n: n[1] % 2 != 0, ((n[0], (n[1] - 1) // 2 if n[1] != -1 else 1) for n in a)))

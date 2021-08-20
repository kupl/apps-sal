def relatively_prime(n, l):
    lst = []
    new = set((x for x in range(1, n + 1) if not n % x))
    for y in l:
        if len(new & set((x for x in range(1, y + 1) if not y % x))) == 1:
            lst.append(y)
    return lst

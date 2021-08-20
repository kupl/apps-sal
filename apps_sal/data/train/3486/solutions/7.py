def find_last(n, m):
    (num, i, L) = (0, 0, [0] * n)

    def ni(i):
        return (i + 1) % len(L)

    def pi(i):
        return (i - 1) % len(L)
    for v in range(2, n + 1):
        num = (num + m) % v
        seen = set(range(len(L)))
        for _ in range(m):
            L[i] += 1
            seen.discard(i)
            i = ni(i)
        for x in seen:
            L[x] += 2
        j = pi(i)
        L[i] += L[j]
        del L[j]
        i = pi(i)
    return (num + 1, L[0])

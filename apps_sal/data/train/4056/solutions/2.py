def leaderboard_sort(L, C):
    for c in C:
        n, m = c.split()
        i = L.index(n)
        L.pop(i)
        L.insert(i - eval(m), n)
    return L

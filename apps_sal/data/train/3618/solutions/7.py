def socialist_distribution(a, n):
    m = sum(a)
    if m < len(a) * n:
        return []
    if m == len(a) * n:
        return [n] * len(a)
    for i in range(sum((n - x for x in a if x < n))):
        a[a.index(max(a))] -= 1
    return [max(x, n) for x in a]

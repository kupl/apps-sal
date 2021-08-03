def socialist_distribution(p, m):
    if sum(p) / len(p) < m:
        return []
    while min(p) < m:
        p[p.index(min(p))] += 1
        p[p.index(max(p))] -= 1
    return p

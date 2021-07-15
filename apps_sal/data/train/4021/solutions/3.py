def elections_winners(a, n):
    m = max(a)
    return sum(x + n > m for x in a) if n else a.count(m) == 1

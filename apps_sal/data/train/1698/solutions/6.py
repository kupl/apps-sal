def dbl_linear(n):
    """Brute force first loop populates the set of u.  The second loop 
    fills any gaps"""
    r = {1}
    while len(r) <= n:
        q = sorted(list(r))
        r.update([e * 2 + 1 for e in q] + [e * 3 + 1 for e in q])
    for _ in range(3):
        q = sorted(list(r))[:n]
        r.update([e * 2 + 1 for e in q] + [e * 3 + 1 for e in q])
    return sorted(list(r))[n]

def dot(n, m):
    return f"\n{' o '.join(['|']*(n+1))}\n".join(['---'.join(['+'] * (n + 1))] * (m + 1))

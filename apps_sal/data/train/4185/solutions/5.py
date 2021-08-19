def sc(width, length, gaps):
    edges = (width + length - 2) * 2
    (q, r) = divmod(edges, gaps + 1)
    return q * (not r)

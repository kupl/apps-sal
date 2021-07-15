def bin_mul(m, n):
    if m < n:
        m, n = n, m
    xs = []
    while m >= 1:
        m, m_r = divmod(m, 2)
        if m_r and n:
            xs.append(n)
        n *= 2
    return sorted(xs, reverse=True)

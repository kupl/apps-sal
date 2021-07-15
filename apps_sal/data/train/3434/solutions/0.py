def bin_mul(m,n):
    if m < n: return bin_mul(n,m)
    if n == 0: return []
    res = []
    while m > 0:
        if m % 2 == 1: res.append(n)
        m = m//2; n *=2
    return res[::-1]

def subsets_parity(n, k):
    while k:
        if not n & 1 and k & 1:
            return 'EVEN'
        (n, k) = (n // 2, k // 2)
    return 'ODD'

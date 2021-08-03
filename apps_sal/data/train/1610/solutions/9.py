def subsets_parity(n, k):
    return 'ODD' if n == k | (n - k) else 'EVEN'

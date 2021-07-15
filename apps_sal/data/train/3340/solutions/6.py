def sharkovsky(a, b):
    def key(n): even = n & -n; return [(even, n // even), (float('inf'), -n)][n == even]
    return key(a) < key(b)

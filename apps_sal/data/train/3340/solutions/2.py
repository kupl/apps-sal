def key(n): return [(0, e := n & -n, n // e), (1, -n)][e == n]
def sharkovsky(a, b): return key(a) < key(b)

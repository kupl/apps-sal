from math import factorial as f
def choose(n, k): return f(n) / (f(k) * f(n - k)) if k <= n else 0

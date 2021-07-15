def f(n): return n - m(f(n-1)) if n else 1

def m(n): return n - f(m(n-1)) if n else 0

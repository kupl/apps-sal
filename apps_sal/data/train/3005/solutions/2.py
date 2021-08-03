def f(n, a=0, b=1): return f(n - 1, b, a + b) if n != -2 else a - 1

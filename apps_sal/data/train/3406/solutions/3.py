f = lambda n: 1 if n == 0 else n - m(f(n - 1))
m = lambda n: 0 if n == 0 else n - f(m(n - 1))

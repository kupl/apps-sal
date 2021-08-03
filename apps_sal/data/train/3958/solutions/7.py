custom_fib = f = lambda s, x, n: f(s[1:] + [sum(s[i]for i in x)], x, n - 1)if n else s[n]

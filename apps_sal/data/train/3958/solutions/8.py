def custom_fib(s, x, n, l=None): return s[n] if len(s) > n else custom_fib((lambda p: s + [sum(p[i] for i in x)])(s[-(l or len(s)):]), x, n, l or len(s))

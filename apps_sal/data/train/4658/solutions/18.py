def max_product(a, n): return __import__("functools").reduce(lambda x, y: x * y, sorted(a)[-n:])

def parameter(n): return (lambda a, b: a * b // __import__('fractions').gcd(a, b))(*[eval(c.join(str(n)))for c in '+*'])

def divisors(n): return (lambda s: len([i for i in range(1, s + 1) if not n % i]) * 2 - (s * s == n))(int(n**0.5))

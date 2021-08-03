def solve(n): return (lambda s: int(max((str(int(s[:i]) - (i < len(s))) + '9' * (len(s) - i)for i, d in enumerate(s, 1)), key=lambda s: (sum(map(int, s)), s))))(str(n))

def solve(a, b): return (lambda c: [c.get(s, 0)for s in b])(__import__('collections').Counter(a))

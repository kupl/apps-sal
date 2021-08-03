def solve(n):
    'We have a regular progression from 11 on'
    return 292 + (n - 11) * 49 if n > 10 else len(set(n - v - x - l + v * 5 + x * 10 + l * 50 for l in range(n + 1) for x in range(n + 1 - l) for v in range(n + 1 - l - x)))

def prime_string(s):
    n = len(s)
    return all((s != s[:i] * (n // i) for i in range(1, n // 2 + 1)))

def solve(arr):
    (ar, v) = (arr[:], lambda p: lambda n: 0 if n % p else 1 + v(p)(n // p))
    return sorted(reversed(sorted(ar, key=v(3))), key=v(2))

def solve(arr):

    def fn(p):
        return lambda n: 0 if n % p else 1 + fn(p)(n // p)
    return sorted(sorted(arr, key=fn(3), reverse=True), key=fn(2))

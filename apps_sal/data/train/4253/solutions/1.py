def solve(n, k):
    return [n] if k == 1 else (lambda r: r[-1] if len(r) else [])(list(filter(lambda a: a[-1] > 0 and a[-1] > a[-2] and (not a[-1] % a[0]), ([j * i for j in range(1, k)] + [int(n - k * (k - 1) / 2 * i)] for i in range(1, int(n / 2) + 1)))))

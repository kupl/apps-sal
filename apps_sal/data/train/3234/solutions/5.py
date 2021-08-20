from functools import reduce


def select_subarray(arr):
    d = {}
    for i in range(len(arr)):
        x = arr[:i] + arr[i + 1:]
        (s, p) = (sum(x), reduce(lambda x, y: x * y, x))
        n = abs(p / s) if s != 0 else float('inf')
        d.setdefault(n, []).append([i, arr[i]])
    r = d.get(min(d))
    return r.pop() if len(r) == 1 else r

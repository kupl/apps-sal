from itertools import product


def solve(arr):
    res = []
    for p, q in product([-1, 0, 1], repeat=2):
        step = (arr[-1] + q - (arr[0] + p)) / (len(arr) - 1)
        if step.is_integer():
            exp = range(arr[0] + p, arr[-1] + q + int(step), int(step)) if step else [arr[0] + p] * len(arr)
            res.append(sum(abs(a - e) if abs(a - e) in (0, 1) else float('inf') for a, e in zip(arr, exp)))
    return min(res) if min(res, default=float('inf')) != float('inf') else -1

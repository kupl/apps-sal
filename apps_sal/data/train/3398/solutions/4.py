def solve(arr):
    n = len(arr)
    (k, s) = (n - 1, n + 1)
    d = arr[k] - arr[0]
    for d in range((d - 2) // k, (d + 2) // k + 1):
        for i in (-1, 0, 1):
            p = [abs(arr[0] + i + d * k - q) for (k, q) in enumerate(arr)]
            if max(p) < 2:
                s = min(s, sum(p))
    return -1 if s > n else s

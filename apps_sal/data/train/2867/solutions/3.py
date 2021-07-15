def fix_progression(arr):
    n, r = len(arr), float('inf')
    for i in range(n - 1):
        x = arr[i]
        for j in range(i + 1, n):
            d = arr[j] - arr[i]
            if d % (j - i):
                continue
            d //= j - i
            x0 = x - i * d
            diff = sum(arr[k] != x0 + k * d for k in range(n))
            r = min(r, diff)
            if r <= 1:
                return r
    return r

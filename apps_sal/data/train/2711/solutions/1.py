def outcome(n, s, k):
    return n <= k <= n * s and (n in (1, k) or sum(outcome(n - 1, s, k - x - 1) for x in range(min(s, k - n + 1))))

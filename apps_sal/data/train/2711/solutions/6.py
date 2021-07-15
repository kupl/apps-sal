def outcome(n, s, k):
    return 0 < k <= s if n == 1 else sum(outcome(n-1, s, k-v) for v in range(1, min(k-(n-1),s)+1) if k-v > 0)

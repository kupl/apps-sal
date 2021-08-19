def outcome(n, s, k):
    if n == 0:
        return k == 0
    return sum((outcome(n - 1, s, k - i) for i in range(1, s + 1))) if n <= k <= s * n else 0

def outcome(n, s, k):
    if n == 1:
        return 1 if 0 < k <= s else 0
    return sum((outcome(n - 1, s, k - j - 1) for j in range(s))) if k > 0 else 0

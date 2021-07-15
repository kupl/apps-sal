def get_score(arr) -> int:
    return sum([0, 40, 100, 300, 1200][n] * (1 + (sum(arr[:i]) // 10)) for i, n in enumerate(arr))

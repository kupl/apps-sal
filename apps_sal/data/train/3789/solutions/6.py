def score_throws(radiuses):
    return sum(
        10 if r < 5 else 5 if r <= 10 else 0
        for r in radiuses
    ) + (bool(radiuses) and all(r < 5 for r in radiuses)) * 100

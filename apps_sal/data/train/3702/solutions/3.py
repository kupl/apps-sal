def olympic_ring(string):
    score = (sum(c in "abdegopqABDOPQR" for c in string) + string.count("B")) // 2
    return next(medal for min_score, medal in (
        (4, "Gold!"),
        (3, "Silver!"),
        (2, "Bronze!"),
        (0, "Not even a medal!"),
    ) if score >= min_score)

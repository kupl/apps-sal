def score_throws(radiuses):
    score = 0
    for r in radiuses:
        if r < 5:
            score += 10
        elif 5 <= r <= 10:
            score += 5
    if radiuses and max(radiuses) < 5:
        score += 100
    return score

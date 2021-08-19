def score_throws(radii):
    score = sum((0 if r > 10 else 5 if r >= 5 else 10 for r in radii))
    if radii and all((r < 5 for r in radii)):
        score += 100
    return score

def score_throws(radii):
    score = sum((0 if r > 10 else 5 if r >= 5 else 10 for r in radii))
    return score + 100 * (score and len(radii) * 10 == score)

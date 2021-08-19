def best_match(goals1, goals2):
    scores = [(zip[0] - zip[1], zip[1], idx) for (idx, zip) in enumerate(zip(goals1, goals2))]
    return sorted(scores, key=lambda y: (y[0], -y[1]))[0][2]

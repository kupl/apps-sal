def best_match(goals1, goals2):
    return min((a - b, -b, i) for i, (a, b) in enumerate(zip(goals1, goals2)))[2]

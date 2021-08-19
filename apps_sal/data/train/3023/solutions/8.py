def best_match(goals1, goals2):
    l = [(i - j, -j) for (i, j) in zip(goals1, goals2)]
    return l.index(min(l))

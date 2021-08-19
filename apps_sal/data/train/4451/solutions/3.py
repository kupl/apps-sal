def golf_score_calculator(*par_score):
    return sum((int(b) - int(a) for (a, b) in zip(*par_score)))

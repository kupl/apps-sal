def golf_score_calculator(par, score):
    return sum(int(b) - int(a) for a, b in zip(par, score))

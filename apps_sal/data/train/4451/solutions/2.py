def golf_score_calculator(par, score):
    return sum(map(int, score)) - sum(map(int, par))

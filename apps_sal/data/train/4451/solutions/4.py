def golf_score_calculator(par_string, score_string):
    return sum(map(int, list(score_string))) - sum(map(int, list(par_string)))

def golf_score_calculator(par_string, score_string):
    return sum(b-a for a,b in zip(map(int, par_string), map(int, score_string)))

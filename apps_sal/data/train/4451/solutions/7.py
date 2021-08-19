def golf_score_calculator(par_string, score_string):
    par_list = list(map(int, par_string))
    score_list = list(map(int, score_string))
    differences = [i - j for (i, j) in zip(score_list, par_list)]
    return sum(differences)
    pass

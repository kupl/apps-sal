def golf_score_calculator(par_stg, score_stg):
    return sum((int(s) - int(p)) for (s, p) in zip(score_stg, par_stg))

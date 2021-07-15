def golf_score_calculator(par_string, score_string):
    score = 0
    for i in range(0,18):
        score -= int(par_string[i]) - int(score_string[i])
    return score

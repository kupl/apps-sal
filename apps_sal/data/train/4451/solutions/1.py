def golf_score_calculator(p, s):
    return sum([int(s[i]) - int(p[i]) for i in range(len(p))])

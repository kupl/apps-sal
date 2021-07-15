def score_throws(radiuses):
    scores = [5 * ((v<5) + (v<=10)) for v in radiuses]
    return sum(scores) + 100 * (len(set(scores)) == 1 and scores[0] == 10)

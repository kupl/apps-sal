def grader(score):
    if 1 >= score >= 0.9:
        score = 'A'
    elif 0.9 > score >= 0.8:
        score = 'B'
    elif 0.8 > score >= 0.7:
        score = 'C'
    elif 0.7 > score >= 0.6:
        score = 'D'
    else:
        score = 'F'
    return score

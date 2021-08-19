def grader(score):
    if float(score) >= 0.9 and float(score) <= 1:
        return 'A'
    if float(score) >= 0.8 and float(score) < 0.9:
        return 'B'
    if float(score) >= 0.7 and float(score) < 0.8:
        return 'C'
    if float(score) >= 0.6 and float(score) < 0.7:
        return 'D'
    return 'F'

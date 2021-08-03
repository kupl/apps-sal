def grader(score):
    if score > 1 or score < 0.6:
        res = 'F'
    elif score >= 0.9:
        res = 'A'
    elif score >= 0.8:
        res = 'B'
    elif score >= 0.7:
        res = 'C'
    elif score >= 0.6:
        res = 'D'
    return res

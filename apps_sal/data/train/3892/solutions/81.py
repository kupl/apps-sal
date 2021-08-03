def grader(score: int):
    if score > 1:
        return 'F'
    elif score >= .9:
        return 'A'
    elif score >= .8:
        return 'B'
    elif score >= .7:
        return 'C'
    elif score >= .6:
        return 'D'
    else:
        return 'F'

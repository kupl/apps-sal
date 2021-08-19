def grader(score):
    if score > 1:
        return 'F'
    elif score > 0.89:
        return 'A'
    elif score > 0.79:
        return 'B'
    elif score > 0.69:
        return 'C'
    elif score > 0.59:
        return 'D'
    elif score < 0.58:
        return 'F'

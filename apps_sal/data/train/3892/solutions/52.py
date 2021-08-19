def grader(s):
    if s > 1 or s < 0.6:
        return 'F'
    elif 1 >= s >= 0.9:
        return 'A'
    elif 0.9 > s >= 0.8:
        return 'B'
    elif 0.8 > s >= 0.7:
        return 'C'
    else:
        return 'D'

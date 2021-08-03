def grader(s):
    print(s)
    if s <= 0.5 or s > 1.0:
        return 'F'
    elif s >= 0.9:
        return 'A'
    elif s >= 0.8:
        return 'B'
    elif s >= 0.7:
        return 'C'
    elif s >= 0.6:
        return 'D'
    else:
        return 'F'

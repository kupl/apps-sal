def grader(s):
    print(s)
    if s > 1 or s < 0.6:
        return 'F'
    if s >= 0.9:
        return 'A'
    if s >= 0.8:
        return 'B'
    if s >= 0.7:
        return 'C'
    return 'D'

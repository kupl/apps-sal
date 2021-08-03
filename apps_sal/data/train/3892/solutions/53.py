def grader(s):
    if s >= 0.9 and s <= 1:
        return 'A'
    if s >= 0.8 and s < 0.9:
        return 'B'
    if s >= 0.7 and s < 0.8:
        return 'C'
    if s >= 0.6 and s < 0.7:
        return 'D'
    return 'F'

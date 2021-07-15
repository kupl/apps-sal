def grader(score):
    if score < 0.6 or score > 1:
        return 'F'
    if 0.6 <= score < 0.7:
        return 'D'
    if 0.7 <= score < 0.8:
        return 'C'
    if 0.8 <= score < 0.9:
        return 'B'
    return 'A'

def grader(score):
    if score < 0.6 or 1 < score:
        return 'F'
    elif 0.9 <= score:
        return 'A'
    elif 0.8 <= score:
        return 'B'
    elif 0.7 <= score:
        return 'C'
    elif 0.6 <= score:
        return 'D'

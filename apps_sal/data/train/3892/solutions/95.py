def grader(score):
    if score < 0.6 or score > 1:
        return 'F'
    elif 0.9 <= score <= 1:
        return 'A'
    elif score >= 0.8:
        return 'B'
    elif score >= 0.7:
        return 'C'
    elif score >= 0.6:
        return 'D'

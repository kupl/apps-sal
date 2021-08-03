def grader(score):
    print(score)
    if score < 0.6 or score > 1:
        return 'F'
    elif 0.9 <= score <= 1:
        return 'A'
    elif 0.8 <= score < 0.9:
        return 'B'
    elif 0.7 <= score < 0.8:
        return 'C'
    elif 0.6 <= score < 0.7:
        return 'D'

def grader(score):
    if score > 1.0 or score < 0.6:
        return 'F'

    for minimum, letter in zip([0.9, 0.8, 0.7, 0.6], list('ABCD')):
        if score >= minimum:
            return letter


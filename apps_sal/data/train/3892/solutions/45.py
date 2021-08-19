def grader(score):
    grade = None
    if score < 0.6 or score > 1:
        grade = 'F'
    else:
        grade = 'A'
        if score < 0.9:
            grade = 'B'
        if score < 0.8:
            grade = 'C'
        if score < 0.7:
            grade = 'D'
    return grade

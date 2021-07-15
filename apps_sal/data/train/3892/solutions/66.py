def grader(score):
    grade = 'F'
    if 1 >= score >= 0.9 :
        grade = 'A'
    elif 0.9 > score >= 0.8:
        grade = 'B'
    elif 0.8 > score >= 0.7:
        grade = 'C'
    elif 0.7 > score >= 0.6:
        grade = 'D'
    return grade


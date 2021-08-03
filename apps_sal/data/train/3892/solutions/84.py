def grader(score):
    grade = 'FFFFFFDCBAA'
    return grade[int(score * 10)] if score <= 1 else 'F'

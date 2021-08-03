def final_grade(exam, projects):
    print((exam, projects))
    grade = 0
    if exam > 90 or projects > 10:
        grade = 100
    elif exam > 75 and projects > 4:
        grade = 90
    elif exam > 50 and projects > 1:
        grade = 75
    return grade

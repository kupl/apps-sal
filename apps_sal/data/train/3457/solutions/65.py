def final_grade(exam, projects):
    grade = 0
    if exam > 90 or projects > 10:
        grade = 100
    elif (exam > 75 and exam <= 90) and projects >= 5:
        grade = 90
    elif exam > 50 and projects >= 2:
        grade = 75
    return grade

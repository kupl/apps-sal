def final_grade(exam, projects):
    grade = [100, 90, 75, 0]
    x = 3
    if exam > 90 or projects > 10:
        x = 0
    elif exam > 75 and projects > 4:
        x = 1
    elif exam > 50 and projects > 1:
        x = 2
    return grade[x]

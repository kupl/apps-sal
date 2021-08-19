def final_grade(exam, projects):
    if exam > 90 or projects > 10:
        return 100
    elif exam > 75 and projects >= 5 and (projects <= 10):
        return 90
    elif exam > 50 and projects >= 2 and (projects <= 10):
        return 75
    else:
        return 0

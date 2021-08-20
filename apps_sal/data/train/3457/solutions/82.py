def final_grade(exam, projects):
    if exam > 90 or projects > 10:
        return 100
    if (exam > 75 and exam <= 90) and (projects >= 5 and projects <= 10):
        return 90
    if exam > 50 and projects >= 2:
        return 75
    else:
        return 0

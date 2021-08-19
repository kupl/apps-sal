def final_grade(exam, projects):
    if exam > 90 or projects > 10:
        return 100
    elif 75 < exam and 5 <= projects:
        return 90
    elif 50 < exam and 2 <= projects:
        return 75
    else:
        return 0

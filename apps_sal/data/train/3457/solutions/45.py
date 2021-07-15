def final_grade(exam, projects):
    if projects > 10 or exam > 90:
        return 100
    elif exam > 75 and projects > 4:
        return 90
    elif exam > 50 and projects > 1:
        return 75
    else:
        return 0

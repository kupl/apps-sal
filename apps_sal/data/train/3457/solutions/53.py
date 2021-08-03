def final_grade(exam, projects):

    if exam > 90 or projects > 10:
        return 100
    elif exam in range(76, 91) and projects >= 5:
        return 90
    elif exam > 50 and projects >= 2:
        return 75
    elif exam <= 50 or projects < 2:
        return 0

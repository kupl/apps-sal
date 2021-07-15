def final_grade(exam, projects):
    if projects > 10:
        return 100
    elif exam > 90:
        return 100
    elif projects >= 5 and exam > 75:
        return 90
    elif projects >= 2 and exam > 50:
        return 75
    else:
        return 0

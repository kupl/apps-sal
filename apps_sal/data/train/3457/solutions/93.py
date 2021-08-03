def final_grade(exam, projects):
    if exam >= 91 or projects > 10:
        return 100
    elif exam >= 76 and projects >= 5:
        return 90
    elif exam >= 51 and projects >= 2:
        return 75
    else:
        return 0
    return  # final grade

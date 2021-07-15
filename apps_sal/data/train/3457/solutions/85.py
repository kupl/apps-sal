def final_grade(exam, projects):
    final = 0
    if exam > 90 or projects > 10:
        final = 100
    elif exam > 75 and projects > 4:
        final = 90
    elif exam > 50 and projects > 1:
        final = 75
    else:
        final = 0
    return final

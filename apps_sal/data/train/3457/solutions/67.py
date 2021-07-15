def final_grade(exam, projects):
    result = 0
    if exam > 90 or projects > 10:
        result = 100
    elif exam > 75 and projects > 4:
        result = 90
    elif exam > 50 and projects > 1:
        result = 75
    else:
        result = 0
    return result

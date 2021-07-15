def final_grade(exam, proj):
    if exam > 90 or proj > 10:
        return 100
    if exam > 75 and proj > 4:
        return 90
    if exam > 50 and proj > 1:
        return 75
    return 0

def final_grade(exam, pro):
    if exam > 90 or pro > 10:
        return 100
    if exam > 75 and pro >= 5:
        return 90
    if exam > 50 and pro >= 2:
        return 75
    else:
        return 0

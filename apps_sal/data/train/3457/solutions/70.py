def final_grade(exam, projects):
    e = exam
    p = projects
    if e > 90 or p > 10:
        return 100
    elif e > 75 and p >= 5:
        return 90
    elif e > 50 and p >= 2:
        return 75
    else:
        return 0

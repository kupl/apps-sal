def final_grade(e, p):
    if e > 90 or p > 10:
        return 100
    if e > 75 and p > 4:
        return 90
    if e > 50 and p > 1:
        return 75
    else:
        return 0

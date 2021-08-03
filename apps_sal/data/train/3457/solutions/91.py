def final_grade(e, p):
    if p > 10 or e > 90:
        return 100
    if p >= 5 and e > 75:
        return 90
    if p >= 2 and e > 50:
        return 75
    return 0

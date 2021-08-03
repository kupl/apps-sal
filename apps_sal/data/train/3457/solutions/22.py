def final_grade(e, p, o=0):
    return 100 if e > 90 or p > 10 else 90 if e > 75 and p > 4 else 75 if e > 50 and p > 1 else 0

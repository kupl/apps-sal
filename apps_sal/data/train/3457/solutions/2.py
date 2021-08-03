def final_grade(x, p):
    return ((x > 90 or p > 10) and 100
            or x > 75 and p >= 5 and 90
            or x > 50 and p >= 2 and 75 or 0)

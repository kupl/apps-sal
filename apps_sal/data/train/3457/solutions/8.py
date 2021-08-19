def final_grade(e, p):
    return {e > 50 and p >= 2: 75, e > 75 and p >= 5: 90, e > 90 or p > 10: 100}.get(True, 0)

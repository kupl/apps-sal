def final_grade(ex, pro):
    if ex > 90 or pro > 10: return 100
    if ex > 75 and pro >= 5: return 90
    if ex > 50 and pro >=2: return 75
    else: return 0# final grade

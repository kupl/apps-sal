def final_grade(exam, pr):
    if exam > 90 or pr > 10:
        return 100
    elif exam > 75 and pr >= 5:
        return 90
    elif exam > 50 and pr >= 2:
        return 75
    return 0

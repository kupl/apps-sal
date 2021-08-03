def final_grade(ex, p):
    if ex > 90 or p > 10:
        return 100
    elif ex > 75 and p >= 5:
        return 90
    elif ex > 50 and p >= 2:
        return 75
    else:
        return 0
  # return # final grade

def final_grade(exam, projects):
    if exam > 90 or projects > 10:
        return 100
    elif (75 < exam) and (5 <= projects):  # <= 10):
        return 90
    elif (50 < exam) and (2 <= projects):  # <5):
        return 75
    # elif projects == 11:
    #    return 100
   # elif exam < 50 and projects > 5:
    #    return 0
    else:
        return 0

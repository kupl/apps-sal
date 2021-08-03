def final_grade(exam, projects):

    if (exam > 90 or projects > 10):
        results = 100
    elif (exam > 75 and projects >= 5):
        results = 90
    elif (exam > 50 and projects >= 2):
        results = 75
    else:
        results = 0

    return results

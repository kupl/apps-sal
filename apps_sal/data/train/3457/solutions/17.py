def final_grade(exam, projects):
    if exam > 90 or projects > 10:
        return 100
    for val in [(75, 5, 90), (50, 2, 75)]:
        if exam > val[0] and projects >= val[1]:
            return val[2]
    return 0

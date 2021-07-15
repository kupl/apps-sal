def final_grade(exam, projects):
    try:
        return {
            exam > 50 and projects >= 2: 75,
            exam > 75 and projects >= 5: 90,
            exam > 90 or projects > 10: 100
        }[True]
    except KeyError:
        return 0

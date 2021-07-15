def final_grade(exam, projects):
    return {exam > 50 and projects > 1: 75,
            exam > 75 and projects > 4: 90,
            exam > 90 or projects > 10: 100}.get(True, 0)

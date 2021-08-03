def final_grade(exam, projects):
    return min((75 * (exam > 50 and projects > 1) + 15 * (exam > 75 and projects > 4)) + 100 * (exam > 90 or projects > 10), 100)

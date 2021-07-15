def final_grade(exam, projects):
    results = [0, 75, 90, 100, 100, 100]
    return results[3 * (exam > 90 or projects > 10) + (exam > 75 and projects >= 5) + (exam > 50 and projects >= 2)]

def final_grade(exam, projects):
    return [0, 75, 90][(exam > 50 and projects > 1) + (exam > 75 and projects > 4)] if exam <= 90 and projects <= 10 else 100

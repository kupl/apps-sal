def final_grade(exam, projects):
    exams, proj, grades = [90, 75, 50, 0], [10, 4, 1, 0], [100, 90, 75, 0]
    for i in range(4):
        if exam > 90 or projects > 10:
            return 100
        if exam > exams[i] and projects > proj[i]:
            return grades[i]
    return 0

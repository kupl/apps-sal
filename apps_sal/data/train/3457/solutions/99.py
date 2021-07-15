def final_grade(exam, projects):
    rubric = [100, 90, 75, 0]
    return rubric[0] if exam > 90 or projects > 10 else rubric[1] if exam > 75 and projects >= 5 else rubric[2] if exam > 50 and projects >= 2 else rubric[3]

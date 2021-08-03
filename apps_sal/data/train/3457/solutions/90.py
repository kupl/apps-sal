def final_grade(exam, projects):
    if int(exam) > 90 or int(projects) > 10:
        final_grade = 100
    elif int(exam) > 75 and int(projects) >= 5:
        final_grade = 90
    elif int(exam) > 50 and int(projects) >= 2:
        final_grade = 75
    else:
        final_grade = 0
    return final_grade

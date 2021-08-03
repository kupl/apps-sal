def final_grade(exam, projects):
    if exam > 90 or projects > 10:
        return 100
    minimums = ((90, 76, 5),
                (75, 51, 2),
                (0, 0, 0))
    return next(score for score, exam_min, projects_min
                in minimums
                if exam_min <= exam and projects_min <= projects)

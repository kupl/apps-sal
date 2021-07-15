def final_grade(exams, projects):
    return 100 if exams >90 or projects>10 else 90 if exams>75 and projects>=5 else 75 if exams>50 and projects>=2 else 0

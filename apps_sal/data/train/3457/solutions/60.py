def final_grade(exam, proj):
    return 100 if exam > 90 or proj > 10 else 90 if exam > 75 and proj >= 5 else 75 if exam > 50 and proj >= 2 else 0

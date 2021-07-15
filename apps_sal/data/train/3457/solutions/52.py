# calculate final grade of student based on grade for an exam and a number of projects
# input - integer for exam grade (0-100), integer for number of projects (0 and above)
# output - integer for final grade


def final_grade(exam, projects):
    if exam > 90 or projects > 10:
        return 100
    if exam > 75 and projects >= 5:
        return 90
    if exam > 50 and projects >= 2:
        return 75
    else:
        return 0

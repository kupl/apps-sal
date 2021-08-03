def grader(score):
    print(score)
    grade = "F"
    if score > 1:
        grade = "F"
    elif score >= 0.9:
        grade = "A"
    elif score >= 0.8:
        grade = "B"
    elif score >= 0.7:
        grade = "C"
    elif score >= 0.6:
        grade = "D"

    return grade

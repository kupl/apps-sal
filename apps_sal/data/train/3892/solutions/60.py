def grader(score):
    grade = float(score)
    if grade >1.0 or grade < 0.6:
        return "F"
    elif grade >= 0.9:
        return "A"
    elif grade >= 0.8:
        return "B"
    elif grade >= 0.7:
        return "C"
    elif grade >= 0.6:
        return "D"


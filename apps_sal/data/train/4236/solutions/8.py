def calculate_grade(scores):

    avg_grade = sum(scores) / len(scores)
    if avg_grade < 60:
        return "F"
    elif avg_grade < 70:
        return "D"
    elif avg_grade < 80:
        return "C"
    elif avg_grade < 90:
        return "B"
    else:
        return "A"

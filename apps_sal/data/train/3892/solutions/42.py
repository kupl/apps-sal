def grader(score):
    if score >= 0.9:
        if score > 1:
            return "F"
        return "A"
    elif score >= 0.8:
        return "B"
    elif score >= 0.7:
        return "C"
    elif score >= 0.6:
        return "D"
    else:
        return "F"


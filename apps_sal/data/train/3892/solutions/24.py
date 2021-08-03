def grader(score):
    if 1 < score or 0.6 > score:
        return "F"
    if score >= 0.9:
        return "A"
    if score >= 0.8:
        return "B"
    if score >= 0.7:
        return "C"
    if score >= 0.6:
        return "D"

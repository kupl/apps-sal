import statistics


def calculate_grade(scores):
    mean = statistics.mean(scores)
    if mean >= 90:
        return "A"
    if mean >= 80:
        return "B"
    if mean >= 70:
        return "C"
    if mean >= 60:
        return "D"
    return "F"

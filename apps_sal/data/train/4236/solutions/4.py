from statistics import mean


def calculate_grade(scores):
    a = mean(scores)
    return 'A' if a >= 90 else 'B' if a >= 80 else 'C' if a >= 70 else 'D' if a >= 60 else 'F'

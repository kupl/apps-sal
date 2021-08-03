def calculate_grade(scores):
    x = sum(scores) / len(scores)
    return 'A' if x >= 90 else 'B' if x >= 80 else 'C' if x >= 70 else 'D' if x >= 60 else 'F'

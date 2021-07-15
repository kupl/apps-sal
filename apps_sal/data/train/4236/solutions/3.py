def calculate_grade(scores):
    s = sum(scores) / len(scores)
    return 'ABCDF'[(s < 90) + (s < 80) + (s < 70) + (s < 60)]

def calculate_grade(scores):
    mean = sum(scores) / len(scores)
    return "ABCDF"[(mean < 90) + (mean < 80) + (mean < 70) + (mean < 60)]

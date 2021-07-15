def calculate_grade(scores):
    import numpy as np
    mean_score = np.mean(scores)
    if mean_score >= 90:
        return "A"
    elif mean_score >= 80:
        return "B"
    elif mean_score >= 70:
        return "C"
    elif mean_score >= 60:
        return "D"
    else:
        return "F"


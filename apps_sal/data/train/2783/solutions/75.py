def get_grade(s1, s2, s3):
    
    mean_score = (s1 + s2 + s3) / 3

    if mean_score >= 90:
        return 'A'
    if mean_score >= 80:
        return 'B'
    if mean_score >= 70:
        return 'C'
    if mean_score >= 60:
        return 'D'
    return "F"


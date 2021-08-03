def get_grade(s1, s2, s3):
    score = (s1 + s2 + s3) / 3
    if score >= 0 and score < 60:
        return 'F'
    if score >= 60 and score < 70:
        return 'D'
    if score >= 70 and score < 80:
        return 'C'
    if score >= 80 and score < 90:
        return 'B'
    if score >= 90 and score <= 100:
        return 'A'

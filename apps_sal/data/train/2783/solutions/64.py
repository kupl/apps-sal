def get_grade(s1, s2, s3):
    score = (s1 + s2 + s3) / 3
    letter = ''
    if score <= 100 and score >= 90:
        letter = 'A'
    elif score < 90 and score >= 80:
        letter = 'B'
    elif score < 80 and score >= 70:
        letter = 'C'
    elif score < 70 and score >= 60:
        letter = 'D'
    elif score < 60:
        letter = 'F'
    return letter

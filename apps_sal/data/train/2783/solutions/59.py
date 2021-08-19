def get_grade(s1, s2, s3):
    result = sum((s1, s2, s3)) / 3
    if result > 90:
        return 'A'
    elif 90 > result >= 80:
        return 'B'
    elif 80 > result >= 70:
        return 'C'
    elif 70 > result >= 60:
        return 'D'
    elif 60 > result >= 0:
        return 'F'

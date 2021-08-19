def get_grade(s1, s2, s3):
    s = s1 + s2 + s3
    s /= 3
    if s >= 90:
        return 'A'
    elif s >= 80:
        return 'B'
    elif s >= 70:
        return 'C'
    elif s >= 60:
        return 'D'
    return 'F'

def get_grade(s1, s2, s3):
    x = (s1 + s2 + s3) / 3
    if x < 60:
        return 'F'
    if x >= 60 and x < 70:
        return 'D'
    if 70 <= x < 80:
        return 'C'
    if 80 <= x < 90:
        return 'B'
    else:
        return 'A'

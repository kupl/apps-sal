def get_grade(s1, s2, s3):
    val = (s1 + s2 + s3) / 3
    if val <= 100 and val >= 90:
        return 'A'
    elif val >= 80 and val < 90:
        return 'B'
    elif val >= 70 and val < 80:
        return 'C'
    elif val >= 60 and val < 70:
        return 'D'
    elif val >= 0 and val < 60:
        return 'F'

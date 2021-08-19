def get_grade(s1, s2, s3):
    result = (s1 + s2 + s3) / 3
    if result >= 90:
        return 'A'
    elif result >= 80 and result < 90:
        return 'B'
    elif result >= 70 and result < 80:
        return 'C'
    elif result >= 60 and result < 70:
        return 'D'
    else:
        return 'F'

def get_grade(s1, s2, s3):
    mean = (s1 + s2 + s3) / 3.0
    if mean >= 70.0:
        if mean < 80.0:
            return 'C'
        elif mean < 90:
            return 'B'
        else:
            return 'A'
    elif mean >= 60:
        return 'D'
    else:
        return 'F'

def get_grade(s1, s2, s3):
    a = (s1 + s2 + s3) / 3
    if a >= 90:
        return 'A'
    elif a >= 80:
        return 'B'
    elif a >= 70:
        return 'C'
    elif a >= 60:
        return 'D'
    else:
        return 'F'

    return

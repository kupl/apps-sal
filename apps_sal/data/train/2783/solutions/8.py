def get_grade(s1, s2, s3):
    m = (s1 + s2 + s3) / 3
    if m > 89:
        return 'A'
    elif m > 79:
        return 'B'
    elif m > 69:
        return 'C'
    elif m > 59:
        return 'D'
    else:
        return "F"


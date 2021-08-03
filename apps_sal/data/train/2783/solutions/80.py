def get_grade(s1, s2, s3):
    print((s1, s2, s3))
    x = (s1 + s2 + s3) / 3
    if x <= 100 and x >= 90:
        return 'A'
    elif x <= 89 and x >= 80:
        return 'B'
    elif x <= 79 and x >= 70:
        return 'C'
    elif x <= 69 and x >= 60:
        return 'D'
    else:
        return 'F'

def get_grade(s1, s2, s3):
    g = (s1 + s2 + s3) / 3
    if g < 60:
        return 'F'
    elif g < 70:
        return 'D'
    elif g < 80:
        return 'C'
    elif g < 90:
        return 'B'
    else:
        return 'A'


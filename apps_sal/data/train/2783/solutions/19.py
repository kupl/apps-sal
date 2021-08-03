from statistics import mean


def get_grade(s1, s2, s3):
    a = mean((s1, s2, s3))
    if a < 60:
        return 'F'
    elif a < 70:
        return 'D'
    elif a < 80:
        return 'C'
    elif a < 90:
        return 'B'
    else:
        return 'A'

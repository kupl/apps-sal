def get_grade(s1, s2, s3):

    mean = (s1 + s2 + s3) / 3

    if 90 <= mean <= 100:
        return 'A'
    if 80 <= mean < 90:
        return 'B'
    if 70 <= mean < 80:
        return 'C'
    if 60 <= mean < 70:
        return 'D'
    if 0 <= mean < 60:
        return 'F'
    else:
        return 'no'

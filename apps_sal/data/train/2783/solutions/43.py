def get_grade(s1, s2, s3):
    av = (int(s1) + int(s2) + int(s3)) / 3
    if int(av) >= 90:
        return 'A'
    if 80 <= int(av) < 90:
        return 'B'
    if 70 <= int(av) < 80:
        return 'C'
    if 60 <= int(av) < 70:
        return 'D'
    if int(av) < 60:
        return 'F'

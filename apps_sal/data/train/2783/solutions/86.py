def get_grade(s1, s2, s3):
    f = int((s1 + s2 + s3) / 3)
    if f in range(90,101):
        return 'A'
    elif f in range(80, 90):
        return 'B'
    elif f in range(70, 80):
        return 'C'
    elif f in range(60, 70):
        return 'D'
    elif f in range(0, 60):
        return 'F'


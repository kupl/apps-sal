def get_grade(s1, s2, s3):
    if (s1 + s2 + s3) / 3 < 60:
        return "F"
    if (s1 + s2 + s3) / 3 < 70:
        return "D"
    if (s1 + s2 + s3) / 3 < 80:
        return "C"
    if (s1 + s2 + s3) / 3 < 90:
        return "B"
    if (s1 + s2 + s3) / 3 <= 100:
        return "A"

def get_grade(s1, s2, s3):
    s = (s1 + s2 + s3) / 3
    if 90 <= s <= 100:
        return 'A'
    if 80 <= s < 90:
        return 'B'
    if 70 <= s < 80:
        return 'C'
    if 60 <= s < 70:
        return 'D'
    if 0 <= s < 60:
        return 'F'

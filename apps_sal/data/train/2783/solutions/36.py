def get_grade(s1, s2, s3):
    a = (s1 + s2 + s3) / 3
    if a >= 90: return "A"
    if a >= 80: return "B"
    if a >= 70: return "C"
    if a >= 60: return "D"
    return "F"

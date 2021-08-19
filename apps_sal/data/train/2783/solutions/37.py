def get_grade(s1, s2, s3):
    # Code here -> OK
    if s1 + s2 + s3 >= 270:
        return "A"
    if ((s1 + s2 + s3 >= 240) & (s1 + s2 + s3 < 270)):
        return "B"
    if ((s1 + s2 + s3 >= 210) & (s1 + s2 + s3 < 240)):
        return "C"
    if ((s1 + s2 + s3 >= 180) & (s1 + s2 + s3 < 210)):
        return "D"
    if ((s1 + s2 + s3 >= 0) & (s1 + s2 + s3 < 180)):
        return "F"
    return "F"

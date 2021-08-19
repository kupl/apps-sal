def get_grade(s1, s2, s3):
    return 'A' if (s1 + s2 + s3) / 3 >= 90 else 'B' if 80 <= (s1 + s2 + s3) / 3 < 90 else 'C' if 70 <= (s1 + s2 + s3) / 3 < 80 else 'D' if 60 <= (s1 + s2 + s3) / 3 < 70 else 'F'

def get_grade(s1, s2, s3):
    avg = sum((s1, s2, s3)) / 3
    return ('F', 'D', 'C', 'B', 'A')[(avg >= 60) + (avg >= 70) + (avg >= 80) + (avg >= 90)]

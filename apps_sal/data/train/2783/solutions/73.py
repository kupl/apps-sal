def get_grade(s1, s2, s3):
    avg = sum((s1, s2, s3)) // 3
    return ['F', 'D', 'C', 'B', 'A'][sum((avg > 59, avg > 69, avg > 79, avg > 89))]

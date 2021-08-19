def get_grade(s1, s2, s3):
    mean = (s1 + s2 + s3) / 3
    for (limit, grade) in [(90, 'A'), (80, 'B'), (70, 'C'), (60, 'D')]:
        if limit <= mean <= 100:
            return grade
    return 'F'

def get_grade(s1, s2, s3):
    grades = {range(60): 'F', range(60, 70): 'D', range(70, 80): 'C', range(80, 90): 'B', range(90, 101): 'A'}
    for x in grades:
        if int((s1 + s2 + s3) / 3) in x:
            return (grades[x])

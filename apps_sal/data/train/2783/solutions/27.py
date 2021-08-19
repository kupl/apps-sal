def get_grade(s1, s2, s3):
    score = (s1 + s2 + s3) / 3
    grades = [[90, 'A'], [80, 'B'], [70, 'C'], [60, 'D'], [0, 'F']]
    for grade in grades:
        if score >= grade[0]:
            return grade[1]

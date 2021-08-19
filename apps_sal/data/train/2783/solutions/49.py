def get_grade(s1, s2, s3):
    mean_grade = (s1 + s2 + s3) / 3
    grade = ''
    if mean_grade >= 0 and mean_grade < 60:
        grade = 'F'
    if mean_grade >= 60 and mean_grade < 70:
        grade = 'D'
    if mean_grade >= 70 and mean_grade < 80:
        grade = 'C'
    if mean_grade >= 80 and mean_grade < 90:
        grade = 'B'
    if mean_grade >= 90 and mean_grade <= 100:
        grade = 'A'
    return grade

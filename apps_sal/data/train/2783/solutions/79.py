def get_grade(s1, s2, s3):
    score = (s1 + s2 + s3) / 3
    grade = ''
    if score >= 90 and score <= 100:
        grade = 'A'
    elif score >= 80 and score < 90:
        grade = 'B'
    elif score >= 70 and score < 80:
        grade = 'C'
    elif score >= 60 and score < 70:
        grade = "D"
    elif score >= 0 and score < 60:
        grade = 'F'
    
    return grade


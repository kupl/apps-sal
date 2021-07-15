def get_grade(s1, s2, s3):
    w=(s1+s2+s3)/3
    if 90 <=w<= 100:
        return'A'
    elif 80<=w<90:
        return'B'
    elif 70<=w<80:
        return'C'
    elif 60<=w<70:
        return'D'
    elif 0<=w<60:
        return'F'


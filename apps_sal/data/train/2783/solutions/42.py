def get_grade(s1, s2, s3):
    # Code here
    s=s1+s2+s3
    res=s/3
    if res >= 90 and res <=100:
        return 'A'
    elif res >=80 and res <=90:
        return 'B'
    elif res >=70 and res <=80:
        return 'C'
    elif res >=60 and res <=70:
        return 'D'
    elif res >=0 and res <=60:
        return 'F'


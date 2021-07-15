def get_grade(s1, s2, s3):
    tg = (s1+s2+s3)/3
    return "F" if tg<60 else "D" if tg<70 else "C" if tg<80 else "B" if tg<90 else "A"

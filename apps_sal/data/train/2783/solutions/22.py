def get_grade(s1, s2, s3):
    a = (s1+s2+s3) / 3
    if 90 <= a <= 100:
        return "A"
    elif 80 <= a < 90:
        return "B"
    elif 70 <= a < 80:
        return "C"
    elif 60 <= a < 70:
        return "D"
    elif 0 <= a < 60:
        return "F"

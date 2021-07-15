def get_grade(s1, s2, s3):
    nota = (s1+s2+s3) / 3
    if nota >= 90:
        return "A"
    elif nota >= 80:
        return "B"
    elif nota >= 70:
        return "C"
    elif nota >= 60:
        return "D"
    else:
        return "F"


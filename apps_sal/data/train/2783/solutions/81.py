def get_grade(s1, s2, s3):
    mean = (s1 + s2 + s3) / 3
    if mean <= 100 and mean > 90:
        return "A"
    elif mean < 90 and mean >= 80:
        return "B"
    elif mean < 80 and mean >= 70:
        return "C"
    elif mean < 70 and mean >= 60:
        return "D"
    else:
        # Code here
        return "F"

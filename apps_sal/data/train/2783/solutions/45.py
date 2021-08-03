def get_grade(s1, s2, s3):
    mean = (s1 + s2 + s3) // 3
    print(mean)
    if mean >= 90:
        return "A"
    elif mean >= 80:
        return "B"
    elif mean >= 70:
        return "C"
    elif mean >= 60:
        return "D"
    else:
        return "F"

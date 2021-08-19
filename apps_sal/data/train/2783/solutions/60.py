def get_grade(s1, s2, s3):
    score = (s1 + s2 + s3) / 3
    if 90 <= score or 100 <= score:
        return "A"
    elif 80 <= score or 90 < score:
        return "B"
    elif 70 <= score or 80 < score:
        return "C"
    elif 60 <= score < 70:
        return "D"
    else:
        #         if 0 <= score or score <60:
        return "F"

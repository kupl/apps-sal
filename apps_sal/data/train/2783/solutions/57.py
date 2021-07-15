def get_grade(s1, s2, s3):
    score = (s1 + s2 + s3) / 3
    return "A"*(90 <= score <= 100) + "B"*(80 <= score < 90) + "C"*(70 <= score < 80) + "D"*(60 <= score < 70) + "F"*(0 <= score < 60)


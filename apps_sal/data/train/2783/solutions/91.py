def get_grade(s1, s2, s3):
    grades = (s1,s2,s3)
    total = sum(grades)
    mean = total / len(grades)
    
    if 100 >= mean >= 90:
        return "A"
    elif 90 > mean >= 80:
        return "B"
    elif 80 > mean >= 70:
        return "C"
    elif 70 > mean >= 60:
        return "D"
    else:
        return "F"
    


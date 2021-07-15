def get_grade(s1, s2, s3):
    m=int((s1+s2+s3)/3)
    if m>=90 and m<=100: return "A"
    elif m>=80 and m<90: return "B"
    elif m>=70 and m<80: return "C"
    elif m>=60 and m<70: return "D"
    else: return "F"


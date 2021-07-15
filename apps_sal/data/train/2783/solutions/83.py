def get_grade(s1, s2, s3):
    x=(s1+s2+s3)/3
    if(x<60):
        return "F"
    if(x<70):
        return "D"
    if(x<80):
        return "C"
    if(x<90):
        return "B"
    return "A"


def get_grade(s1, s2, s3):
    # Code here
    avg=((s1+s2+s3)/3)
    if(avg>90):
        return "A"
    elif(80<=avg<90):
        return "B"
    elif(70<=avg<80):
        return "C"
    elif(60<=avg<70):
        return "D"
    return "F"


def get_grade(s1, s2, s3):
    if 90<=(s1+s2+s3)/3 <=100 :
        return "A"
    if 80<=(s1+s2+s3)/3 <90 :
        return "B"
    if 70<=(s1+s2+s3)/3 <80 :
        return "C"
    if 60<=(s1+s2+s3)/3 <70 : 
        return "D"
    if 0<=(s1+s2+s3)/3 <=60 : 
        return "F"

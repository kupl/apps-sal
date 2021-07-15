def get_grade(s1, s2, s3):
    a = (s1 + s2 + s3) /3
    if a >=0 and a < 60:
        return 'F'
    elif a >=60 and a < 70:
        return 'D'
    elif a >=70 and a < 80:
        return 'C'
    elif a >=80 and a < 90:
        return 'B'
    else:
        return 'A'
    
    
    
   


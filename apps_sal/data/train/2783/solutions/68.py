def get_grade(s1, s2, s3):
    ave = (s1 + s2 + s3) / 3
    if (ave >= 90) and (ave <= 100):
        return('A')
    elif (ave >= 80) and (ave < 90):
        return('B')
    elif (ave >= 70) and (ave < 80):
        return('C')
    elif (ave >= 60) and (ave < 70):
        return('D')
    else:
        return('F')

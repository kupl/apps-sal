def compare(s1,s2):
    sum1 = sum2 = 0
    if s1 != None and s1.isalpha() :
        for c in s1.upper() :
            sum1 += ord(c)
    if s2 != None and s2.isalpha() :   
       for c in s2.upper() :
            sum2 += ord(c)
    return sum1 == sum2

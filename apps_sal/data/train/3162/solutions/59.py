def compare(s1, s2):
    if s1 == None or s2 == None:
        return True
    if s1.isalpha() == False and s2.isalpha() == False:
        return True
    if s1.isalpha() == False and s2.isalpha() == True:
        return False
    if s2.isalpha() == False and s1.isalpha() == True:
        return False

    sum_s1 = 0
    sum_s2 = 0
    for ele in s1.upper():
        sum_s1 += ord(ele)
    for ele in s2.upper():
        sum_s2 += ord(ele)

    if sum_s1 == sum_s2:
        return True
    else:
        return False

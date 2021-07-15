def lowercase_count(strng):
    a = 0
    for x in strng:
        if x.islower() == True:
            a = a + 1
    return a

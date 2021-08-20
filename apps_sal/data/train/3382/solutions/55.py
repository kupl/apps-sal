def lowercase_count(strng):
    num = 0
    for chr in strng:
        if chr.islower() == True:
            num += 1
    return num

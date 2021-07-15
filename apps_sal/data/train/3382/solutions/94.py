def lowercase_count(strng):
    ctr = 0
    for i in strng:
        if i.islower():
            ctr+=1
    return ctr


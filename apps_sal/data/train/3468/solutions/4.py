def scramble(s1,s2):
    dct={}
    for l in s1:
        if l not in dct:
            dct[l]=1
        else:
            dct[l] +=1
    for l in s2:
        if l not in dct or dct[l] < 1:
            return False
        else:
            dct[l] -= 1
    return True

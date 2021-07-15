def scramble(s1, s2):
    d1, d2 = {}, {}
    for i in s1:
        if i not in d1:
            d1[i] = 1
        else:
            d1[i] += 1
    
    for i in s2:
        if i not in d2:
            d2[i] = 1
        else:
            d2[i] += 1
            
    for key in list(d2.keys()):
        if not key in list(d1.keys()) or d1[key]< d2[key]:
            return False
    return True


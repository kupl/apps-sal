def scramble(s1, s2):
    s1ct = {}
    for ltr in s1:
        if ltr in s1ct.keys():
            s1ct[ltr] += 1
        else:
            s1ct[ltr] = 1
    s2ct = {}
    for ltr in s2:
        if ltr in s2ct.keys():
            s2ct[ltr] += 1
        else:
            s2ct[ltr] = 1
    for ltr in s2ct.keys():
        if ltr not in s1ct.keys():
            return False
        if s2ct[ltr] > s1ct[ltr]:
            return False
    return True

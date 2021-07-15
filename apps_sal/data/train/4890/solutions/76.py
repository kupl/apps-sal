def find_difference(a, b):
    print((a,b))
    resulta = 1
    resultb = 1
    for aa in a:
        resulta = aa * resulta
    print((resulta, 'resulta'))
    for bb in b:
        resultb = bb * resultb
    print((resultb, 'resultb'))
    if resulta > resultb:
        return resulta - resultb
    else:
        return resultb - resulta



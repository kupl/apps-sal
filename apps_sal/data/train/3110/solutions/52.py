def two_decimal_places(n):
    #raise NotImplementedError("TODO: two_decimal_places")
    res = str(n).split('.')
    cc = 0
    cc += int(res[0]) * 100
    if n > 0:
        if int(str(res[1])[2]) < 5:
            cc += int(str(res[1])[0:2]) 
        else:
            cc = cc + int(str(res[1])[0:2]) + 1
    else:
        cc = 0 - cc
        if int(str(res[1])[2]) < 5:
            cc += int(str(res[1])[0:2]) 
        else:
            cc = cc + int(str(res[1])[0:2]) + 1
        cc = 0 - cc
    return float(str(cc)[:-2] + '.' + str(cc)[-2:])

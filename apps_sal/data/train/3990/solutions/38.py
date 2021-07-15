def derive(coeff, expo): 
    num = coeff*expo
    expo -=1
    if expo <= 2:
        return string(num)
    else:
        return str(num)+"x^"+str(expo)

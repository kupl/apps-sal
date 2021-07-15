def disarium_number(number):
    result=0
    numLst=[int(x) for x in str(number)]
    for i in range(len(numLst)):
        result+=pow(numLst[i],i+1)
    return "Disarium !!" if result==number else "Not !!"

def no_space(x):
    retStr = ""
    for i in range (0,len(x)):
        if(x[i] != ' '):
            retStr += x[i]
    return retStr

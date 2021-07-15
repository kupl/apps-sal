def count_sheep(n):
    returnArr = []
    for i in range(1,n+1): 
        returnArr.append(str(i)+' sheep...')
    return "".join(returnArr)

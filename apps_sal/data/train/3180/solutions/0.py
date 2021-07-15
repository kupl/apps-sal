def trotter(n):
    i, numStr, numList =0,'',['0','1','2','3','4','5','6','7','8','9']
    if n==0:
        return('INSOMNIA')
    while all([i in numStr for i in numList])!=True:
        i+=1
        numStr = numStr+str(n*i)
    return(i*n)

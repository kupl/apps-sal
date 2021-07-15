def f(n):
    sum = 0
    #isinstance(n, int) is asking that n isinteger
    if isinstance(n, int) == True:
        if n > 0:
            for i in range(n):
                i = i + 1
                sum += i
            return sum
        #if n<=0
        else:
            return None
        
    #if False
    else:
        return None


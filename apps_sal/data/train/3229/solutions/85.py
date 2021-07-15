def am_i_wilson(n):
    if n==5 or n==13 or n==563:
        return True
    else:
        return False
    '''
    if n <= 2:
        return False
    fact=math.factorial(n-1)
    if (fact+1)%n==0:
        x = (fact+1)%(n**2)
        if x==0:
            return True
        else:
            return False
    else:
        return False
    '''

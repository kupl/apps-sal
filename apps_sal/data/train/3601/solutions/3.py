def find_nb(m):
    '''
    n cube sum m = (n*(n+1)//2)**2
    then n**2 < 2*m**0.5 < (n+1)**2
    and we can proof that for any n, 0.5 > (2*m**0.5)**0.5 - n**2 > 2**0.5 - 1 > 0.4
    '''
    n = int((2*m**0.5)**0.5)
    if (n*(n+1)//2)**2 != m: return -1
    return n

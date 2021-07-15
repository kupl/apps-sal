def sum_mul(n, m):
    if n > 0 and m > 0 :
        i = [i for i in range (n,m,n)]
        return sum(i) if i != [] else 0
    else :
        return 'INVALID'
    


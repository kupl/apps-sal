def sum_mul(n, m):
    if(n<=0 or m<=0):
        return "INVALID"
    else:
        s=0
        for i in range(1,m):
            j=i*n
            if(j<m):
                s+=j
    return s


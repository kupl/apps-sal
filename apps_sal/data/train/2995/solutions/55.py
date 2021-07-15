def sum_mul(n, m):
    if n<=0 or 0>=m: return "INVALID"
    elif n>m:return 0
    else:
        c=0
        x=1
        while x*n<m:
            c+=x*n
            x+=1
        return c


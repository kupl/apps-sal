def sum_mul(n, m):
    print(m,n)
    if m<=0 or n<=0:
        return "INVALID"
    else:
        a=list(range(n,m,n))
        return sum(a)

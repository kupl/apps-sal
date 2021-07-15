def sum_mul(n, m):
    return 'INVALID' if m<=0 or n<=0 else sum([x for x in range(n,m) if x%n==0])

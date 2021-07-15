def sum_mul(n, m):
    return sum(range(n,m,n)) if 0<n<m else 'INVALID' if n*m<=0 else 0  

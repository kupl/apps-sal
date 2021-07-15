def sum_mul(n, m):
    total = 0
    if n <= 0 or m <= 0:
        return 'INVALID'
    try:
        for n in  range(n,m,n):
            total += n
        return total 
    except:
        return 'INVALID'

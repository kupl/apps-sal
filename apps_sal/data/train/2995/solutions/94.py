def sum_mul(n, m):    
    if n <= 0 or m <= 0:
        return 'INVALID'
    try:
        ans = [i for i in range(n, m) if i % n == 0]
        return sum(ans)
    except:
        return 'INVALID'

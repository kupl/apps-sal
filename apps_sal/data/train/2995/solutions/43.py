def sum_mul(n, m):
    result = 0
    if m <= 0 or n <= 0:
        return "INVALID"
    elif  n > m or m == n:
        return 0
    for i in range(n,m,n):
        result+=i
    return result


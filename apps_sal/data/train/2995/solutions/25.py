def sum_mul(n, m):
    result = 0
    if n > 0 < m:
        try:
            for num in range(n, m, n):
                result += num
            return result
        except:
            return 'INVALID'
    else:
        return 'INVALID'

def sum_mul(n, m):
    sum = 0
    for i in range(1,m):
        try:
            if i % n == 0 and m > 0 and n > 0:
                sum += i
        except ZeroDivisionError:
            continue
        
    return sum if n > 0 and m > 0 else 'INVALID'

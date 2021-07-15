def round_to_next5(n):
    if n == 0:
        return 0
    
    if n % 5 == 0:
        return n

    sum1 = n // 5

    if sum1 == 0:
        return 5

    return (sum1+1) * 5

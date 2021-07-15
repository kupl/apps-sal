def dig_pow(n, p):
    digits = [int(d) for d in str(n)]
    
    sum = 0
    for i, d in enumerate(digits):
        sum += d ** (p+i)
    
    if sum % n == 0:
        return sum / n
    else:
        return -1

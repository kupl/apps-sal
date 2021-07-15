def zeros(n):
    result = 0
    power = 1
    while True:
        if 5 ** power > n:
            break
        result += n // (5 ** power)
        power += 1
    
    return result


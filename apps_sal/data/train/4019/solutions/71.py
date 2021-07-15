def max_multiple(divisor, bound):
    sum = 0
    for i in range(1, bound+1):
        if i%divisor == 0:
            sum = i
    return sum


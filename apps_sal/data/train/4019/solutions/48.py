def max_multiple(divisor, bound):
    num = []
    for x in range(divisor, bound+1):
        if x % divisor == 0 and x <= bound and x > 0:
            num.append(x)
    return max(num)
        


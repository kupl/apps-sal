def max_multiple(divisor, bound):
    r=[]
    for i in range(bound+1):
        if i%divisor == 0:
            r.append(i)
    return max(r)


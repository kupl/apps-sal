def max_multiple(divisor, bound):
    a = []
    for i in range(1,bound+1):
        if i % divisor == 0:
            a.append(i)
    return (max(a))

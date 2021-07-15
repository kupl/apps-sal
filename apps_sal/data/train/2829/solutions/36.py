def array_madness(a,b):
    print(a, b)
    sum1 = 0
    sum2 = 0
    for n in  a:
        sum1 += n**2
    for n in b:
        sum2 += n**3
    print(sum1, sum2)
    if sum1 > sum2:
        return True
    else:
        return False

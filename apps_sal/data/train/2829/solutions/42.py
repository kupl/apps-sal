def array_madness(a, b):
    sum1 = 0
    sum2 = 0
    for x in a:
        sum1 += (x ** 2)
    for x in b:
        sum2 += (x ** 3)
    if(sum1 > sum2):
        return True
    else:
        return False

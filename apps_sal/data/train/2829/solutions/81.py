def array_madness(a,b):
    sum1 = 0
    sum2 = 0
    for i in a:
        x = i ** 2
        sum1 += x
    for j in b:
        y = j ** 3
        sum2 += y
    if sum1 > sum2:
        return True
    else:
        return False

def array_madness(a, b):
    sum1 = 0
    sum2 = 0
    for i in a:
        sq = i**2
        sum1 = sum1 + sq
    for j in b:
        cu = j**3
        sum2 = sum2 + cu
    if sum1 > sum2:
        return True
    else:
        return False

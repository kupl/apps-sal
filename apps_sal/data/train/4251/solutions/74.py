def difference_of_squares(n):
    sume1, sume2 = 0, 0
    for i in range(1, n + 1):
        sume1 += i
        sume2 += (i**2)
    sume1 = sume1**2
    return sume1 - sume2

def zeros(n):
    zeros = 0
    tmp = n
    while tmp >= 1:
        tmp /= 5
        zeros += int(tmp)
    return zeros

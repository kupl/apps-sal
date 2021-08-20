import math


def balanced_num(number):
    s = []
    while number > 0:
        d = number % 10
        s.append(d)
        number = math.floor(number / 10)
    l = len(s)
    m = (l - 1) / 2
    left = math.floor(m)
    right = math.ceil(m)
    leftSum = 0
    rightSum = 0
    for i in range(l):
        n = s[i]
        if i < left:
            leftSum += n
        elif i > right:
            rightSum += n
    if rightSum == leftSum:
        return 'Balanced'
    return 'Not Balanced'

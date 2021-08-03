import math


def list_squared(m, n):
    res = []
    for num in range(m, n):
        add = 0
        for i in range(1, math.ceil(math.sqrt(num))):
            if num % i == 0:
                add += i**2 + (num // i)**2
        if math.sqrt(num).is_integer():
            add += num
        if math.sqrt(add).is_integer():
            res.append([num, add])
    return res

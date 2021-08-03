import math as m


def IsPrime(a):
    if a == 1:
        return False
    for i in range(2, int(m.sqrt(a) + 1)):
        if a % i == 0:
            return False
    return True


def algorithm(a):
    while a != 4:
        sum = 0
        for j in str(a):
            sum += int(j)**2
        a = sum
        if a == 1:
            return True
    return False


def solve(a, b):
    counter = 0
    for i in range(a, b):
        if IsPrime(i):
            if algorithm(i):
                counter += 1
    return counter

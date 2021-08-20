import math


def gap(g, m, n):
    first = m
    second = m
    end = False
    while not end:
        for i in range(first, n + 1):
            if i == n:
                end = True
                break
            if isPrime(i):
                first = i
                second = i
                for j in range(first + 1, n + 1):
                    if isPrime(j):
                        second = j
                        break
                    elif j == n:
                        end = True
                break
        if second - first == g:
            print([first, second])
            return [first, second]
        else:
            first = second
    return None


def isPrime(n):
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

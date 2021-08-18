import math


def prime(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return -1
    return 1


def perfect(n):
    if math.sqrt(n) == int(math.sqrt(n)):
        return -1
    else:
        return 1


def semiprime(n):
    temp = []
    for i in range(2, n):
        if n % i == 0:
            temp.append(i)
            if len(temp) > 2:
                return -1
    if len(temp) == 1:
        return -1
    if len(temp) == 2:
        if prime(temp[0]) == 1 and prime(temp[1]) == 1:
            return 1


t = int(input())
for _ in range(t):
    n = int(input())
    check = 0
    for i in range(2, n // 2 + 1):
        if semiprime(i) == 1 and semiprime(n - i) == 1:
            check = 1
            break
    if check > 0:
        print('YES')
    else:
        print('NO')

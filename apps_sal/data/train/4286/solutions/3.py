def solve(n):
    i = 2
    if n % 2 == 0:
        i = 1
    if IsPrime(n):
        return n
    while True:
        temp = n - i
        if IsPrime(temp):
            return temp
        temp = n + i
        if IsPrime(temp):
            return temp
        i += 2


def IsPrime(n):
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5), 2):
        if n % i == 0:
            return False
    return True

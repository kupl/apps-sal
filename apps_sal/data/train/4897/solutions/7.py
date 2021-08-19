def check(n):
    set1 = set()
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            set1.add(i)
            set1.add(n // i)
    return set1


def binary_gcd(x, y):
    if x == 0 and y == 0:
        return 0
    elif x == 0 and y != 0:
        a = y
    elif y == 0 and x != 0:
        a = x
    else:
        a = max(check(abs(x)) & check(abs(y)))
    num = 0
    while a != 0:
        a = a & a - 1
        num += 1
    return num

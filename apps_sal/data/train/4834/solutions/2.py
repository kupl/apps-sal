def prime(a):
    if a == 2:
        return True
    if a < 2 or a % 2 == 0:
        return False
    return not any((a % x == 0 for x in range(3, int(a ** 0.5) + 1, 2)))


def backwardsPrime(start, nd):
    return [x for x in range(start, nd + 1) if str(x) != str(x)[::-1] and prime(x) and prime(int(str(x)[::-1]))]

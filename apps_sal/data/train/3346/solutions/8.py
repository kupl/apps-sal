def isPrime(x):
    x = int(x)
    if x == 2:
        return True
    if x == 1:
        return False
    if x in (3, 5, 7):
        return True
    if x % 2 == 0 or x % 3 == 0 or x % 5 == 0 or (x % 7 == 0):
        return False
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return False
    return True


def gap(gap, start, end):
    for i in range(start, end + 1):
        if isPrime(i) and isPrime(i + gap) and (i + gap <= end):
            good = True
            for j in range(i + 1, i + gap):
                if isPrime(j):
                    good = False
                    break
            if good:
                return [i, i + gap]
    return None

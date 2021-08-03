def isPrime(x):
    x = int(x)
    if x == 2:
        return True
    if x == 1:
        return False
    if x in (3, 5, 7):
        return True
    if x % 2 == 0 or x % 3 == 0 or x % 5 == 0 or x % 7 == 0:
        return False
    for i in range(2, int(x**.5) + 1):
        if x % i == 0:
            return False
    return True


def gap(gap, start, end):
    if start % 2 == 0:
        start += 1
    for i in range(start, end + 1, 2):
        if i + gap > end:
            break
        if isPrime(i) and isPrime(i + gap):
            good = True
            for j in range(i + 1, i + gap):
                if isPrime(j):
                    good = False
                    break
            if good:
                return [i, i + gap]
    return None

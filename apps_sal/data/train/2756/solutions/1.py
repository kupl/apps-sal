def search_permMult(nMax, k):
    x = 0
    for i in range(1000, nMax // k):
        if SameDigits(i * k, i):
            x += 1
    return x


def SameDigits(a, b):
    return sorted(list(str(a))) == sorted(list(str(b)))

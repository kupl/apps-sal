def cycle(n) :
    if n % 2 and n % 5:
        for i in range(1, n):
            if pow(10, i, n) == 1:
                return i
    return -1

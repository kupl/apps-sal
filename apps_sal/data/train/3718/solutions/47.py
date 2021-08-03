def divisors(n):
    list_1 = []
    for x in range(1, n + 1):
        if n % x == 0:
            list_1.append(x)
    length = len(list_1)
    return length

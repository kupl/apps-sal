def nb_dig(n, d):
    result = 1 if d == 0 else 0

    for k in range(1, n + 1):
        x = k * k
        while x:
            if x % 10 == d:
                result += 1
            x //= 10

    return result


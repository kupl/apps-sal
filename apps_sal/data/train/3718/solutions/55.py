def divisors(n):
    k = 1
    for i in range(1, int(n/2)+1):
        if n % i == 0:
            k += 1

    return k

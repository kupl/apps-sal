def divisors(n):
    ret = 1

    for i in range(1, n):
        if n % i == 0:
            ret += 1

    return ret
